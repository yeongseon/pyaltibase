from __future__ import annotations

import unittest
from unittest.mock import patch

import pyaltibase
from pyaltibase.connection import Connection
from pyaltibase.cursor import Cursor
from pyaltibase.exceptions import InterfaceError, ProgrammingError
from pyaltibase.config import ConnectionConfig
from pyaltibase.protocol import build_connection_string
from tests.fakes import FakePyodbcModule


class APITestCase(unittest.TestCase):
    def test_build_connection_string_for_direct_connection(self) -> None:
        config = ConnectionConfig(
            host="localhost",
            port=20300,
            database="sample",
            user="sys",
            password="manager",
            dsn=None,
            driver="ALTIBASE_HDB_ODBC_64bit",
            autocommit=False,
            login_timeout=None,
            nls_use="MS949",
            long_data_compat=True,
            options={"ApplicationName": "pyaltibase"},
        )

        value = build_connection_string(config)

        self.assertIn("DRIVER=ALTIBASE_HDB_ODBC_64bit", value)
        self.assertIn("Server=localhost", value)
        self.assertIn("PORT=20300", value)
        self.assertIn("Database=sample", value)
        self.assertIn("UID=sys", value)
        self.assertIn("PWD=manager", value)
        self.assertIn("NLS_USE=MS949", value)
        self.assertIn("LongDataCompat=on", value)
        self.assertIn("ApplicationName=pyaltibase", value)

    def test_connect_cursor_execute_and_transactions(self) -> None:
        fake_pyodbc = FakePyodbcModule()

        with patch("pyaltibase.connection.import_module", return_value=fake_pyodbc):
            connection = pyaltibase.connect(database="sample", password="manager", login_timeout=5)

            self.assertIsInstance(connection, Connection)
            self.assertFalse(connection.autocommit)
            self.assertEqual(connection.native_connection.timeout, 5)

            cursor = connection.cursor()
            self.assertIsInstance(cursor, Cursor)
            cursor.execute("SELECT ?", [1])
            self.assertEqual(cursor.fetchone(), (1,))
            self.assertEqual(cursor.fetchall(), [(2,)])

            cursor.executemany("INSERT INTO t VALUES (?)", [(1,), (2,)])
            self.assertEqual(cursor.rowcount, 2)

            connection.commit()
            connection.rollback()
            self.assertEqual(connection.native_connection.commit_calls, 1)
            self.assertEqual(connection.native_connection.rollback_calls, 1)

    def test_closed_connection_rejects_cursor_creation(self) -> None:
        fake_pyodbc = FakePyodbcModule()

        with patch("pyaltibase.connection.import_module", return_value=fake_pyodbc):
            connection = pyaltibase.connect()
            connection.close()

            with self.assertRaises(InterfaceError):
                connection.cursor()

    def test_mapping_parameters_are_rejected(self) -> None:
        fake_pyodbc = FakePyodbcModule()

        with patch("pyaltibase.connection.import_module", return_value=fake_pyodbc):
            connection = pyaltibase.connect()
            cursor = connection.cursor()

            with self.assertRaises(ProgrammingError):
                cursor.execute("SELECT ?", {"value": 1})


if __name__ == "__main__":
    unittest.main()
