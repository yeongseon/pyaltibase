from __future__ import annotations

import unittest

import pyaltibase


class ExceptionsTestCase(unittest.TestCase):
    def test_pep249_exception_hierarchy(self) -> None:
        self.assertTrue(issubclass(pyaltibase.Warning, Exception))
        self.assertTrue(issubclass(pyaltibase.Error, Exception))
        self.assertTrue(issubclass(pyaltibase.InterfaceError, pyaltibase.Error))
        self.assertTrue(issubclass(pyaltibase.DatabaseError, pyaltibase.Error))
        self.assertTrue(issubclass(pyaltibase.DataError, pyaltibase.DatabaseError))
        self.assertTrue(issubclass(pyaltibase.OperationalError, pyaltibase.DatabaseError))
        self.assertTrue(issubclass(pyaltibase.IntegrityError, pyaltibase.DatabaseError))
        self.assertTrue(issubclass(pyaltibase.InternalError, pyaltibase.DatabaseError))
        self.assertTrue(issubclass(pyaltibase.ProgrammingError, pyaltibase.DatabaseError))
        self.assertTrue(issubclass(pyaltibase.NotSupportedError, pyaltibase.DatabaseError))

    def test_database_error_repr_includes_optional_fields(self) -> None:
        error = pyaltibase.DatabaseError("boom", errno=7, sqlstate="HY000")

        self.assertEqual(repr(error), "DatabaseError('boom', errno=7, sqlstate='HY000')")

    def test_warning_and_error_repr(self) -> None:
        warning = pyaltibase.Warning("warn", code=1)
        error = pyaltibase.Error("err", code=2)

        self.assertEqual(warning.code, 1)
        self.assertEqual(error.code, 2)
        self.assertEqual(repr(warning), "Warning('warn')")
        self.assertEqual(repr(error), "Error('err')")

    def test_database_error_repr_without_optional_fields(self) -> None:
        error = pyaltibase.DatabaseError("boom")

        self.assertEqual(repr(error), "DatabaseError('boom')")


if __name__ == "__main__":
    unittest.main()
