from __future__ import annotations

import datetime
import unittest
from typing import Any, cast

import pyaltibase


class TypesTestCase(unittest.TestCase):
    def test_type_objects_compare_to_type_codes(self) -> None:
        self.assertEqual(pyaltibase.STRING, 1)
        self.assertEqual(pyaltibase.STRING, 12)
        self.assertEqual(pyaltibase.BINARY, -2)
        self.assertEqual(pyaltibase.BINARY, -3)
        self.assertEqual(pyaltibase.BINARY, -4)
        self.assertEqual(pyaltibase.NUMBER, 2)
        self.assertEqual(pyaltibase.NUMBER, 3)
        self.assertEqual(pyaltibase.NUMBER, 4)
        self.assertEqual(pyaltibase.NUMBER, 5)
        self.assertEqual(pyaltibase.NUMBER, 6)
        self.assertEqual(pyaltibase.NUMBER, 7)
        self.assertEqual(pyaltibase.NUMBER, 8)
        self.assertEqual(pyaltibase.NUMBER, -5)
        self.assertEqual(pyaltibase.DATETIME, 91)
        self.assertEqual(pyaltibase.DATETIME, 92)
        self.assertEqual(pyaltibase.DATETIME, 93)
        self.assertEqual(pyaltibase.ROWID, 15)

    def test_constructors(self) -> None:
        self.assertEqual(pyaltibase.Date(2026, 3, 12), datetime.date(2026, 3, 12))
        self.assertEqual(pyaltibase.Time(8, 30, 0), datetime.time(8, 30, 0))
        self.assertEqual(
            pyaltibase.Timestamp(2026, 3, 12, 8, 30, 0),
            datetime.datetime(2026, 3, 12, 8, 30, 0),
        )
        self.assertEqual(pyaltibase.Binary("abc"), b"abc")

    def test_tick_constructors_and_binary_type_validation(self) -> None:
        ticks = 1_741_769_200

        self.assertEqual(pyaltibase.DateFromTicks(ticks), datetime.date.fromtimestamp(ticks))
        self.assertEqual(
            pyaltibase.TimeFromTicks(ticks), datetime.datetime.fromtimestamp(ticks).time()
        )
        self.assertEqual(
            pyaltibase.TimestampFromTicks(ticks), datetime.datetime.fromtimestamp(ticks)
        )

        with self.assertRaises(TypeError):
            pyaltibase.Binary(cast(Any, 123))

    def test_dbapi_type_dunders_and_binary_inputs(self) -> None:
        self.assertEqual(pyaltibase.STRING, pyaltibase.STRING)
        self.assertNotEqual(pyaltibase.STRING, pyaltibase.BINARY)
        self.assertNotEqual(pyaltibase.STRING, "x")
        self.assertEqual(hash(pyaltibase.STRING), hash(pyaltibase.STRING))
        self.assertEqual(repr(pyaltibase.STRING), "DBAPIType('STRING')")
        self.assertEqual(pyaltibase.Binary(b"abc"), b"abc")
        self.assertEqual(pyaltibase.Binary(bytearray(b"abc")), b"abc")


if __name__ == "__main__":
    _ = unittest.main()
