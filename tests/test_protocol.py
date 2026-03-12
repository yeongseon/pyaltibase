from __future__ import annotations

import unittest

from pyaltibase.config import ConnectionConfig
from pyaltibase.protocol import build_connection_string


class ProtocolTestCase(unittest.TestCase):
    def test_dsn_connection_string(self) -> None:
        config = ConnectionConfig(
            dsn="ALTIBASE_TEST",
            user="sys",
            password="manager",
            options={"ApplicationName": "test-suite"},
        )

        value = build_connection_string(config)

        self.assertEqual(
            value,
            "DSN=ALTIBASE_TEST;UID=sys;PWD=manager;LongDataCompat=on;ApplicationName=test-suite;",
        )

    def test_values_with_spaces_and_braces_are_escaped(self) -> None:
        config = ConnectionConfig(
            driver="ALTIBASE_HDB_ODBC_64bit",
            host="localhost",
            port=20300,
            database="sample name",
            user="sys",
            password="pw}1",
            nls_use="UTF 8",
        )

        value = build_connection_string(config)

        self.assertIn("Database={sample name}", value)
        self.assertIn("PWD={pw}}1}", value)
        self.assertIn("NLS_USE={UTF 8}", value)

    def test_boolean_options_are_stringified_and_none_is_skipped(self) -> None:
        config = ConnectionConfig(options={"Pooling": True, "Ignored": None})

        value = build_connection_string(config)

        self.assertIn("Pooling=1", value)
        self.assertNotIn("Ignored", value)


if __name__ == "__main__":
    unittest.main()
