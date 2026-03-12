"""pyaltibase public DB-API surface."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .exceptions import (
    DatabaseError,
    DataError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    Warning,
)
from .types import (
    BINARY,
    DATETIME,
    NUMBER,
    ROWID,
    STRING,
    Binary,
    Date,
    DateFromTicks,
    Time,
    TimeFromTicks,
    Timestamp,
    TimestampFromTicks,
)

if TYPE_CHECKING:
    from .connection import Connection

__version__ = "0.1.0"

apilevel = "2.0"
threadsafety = 1
paramstyle = "qmark"


def connect(
    host: str = "localhost",
    port: int = 20300,
    database: str = "",
    user: str = "sys",
    password: str = "",
    dsn: str | None = None,
    driver: str = "ALTIBASE_HDB_ODBC_64bit",
    login_timeout: int | None = None,
    nls_use: str | None = None,
    long_data_compat: bool = True,
    **kwargs: object,
) -> Connection:
    """Create an Altibase connection object."""
    from .connection import Connection

    return Connection(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
        dsn=dsn,
        driver=driver,
        login_timeout=login_timeout,
        nls_use=nls_use,
        long_data_compat=long_data_compat,
        **kwargs,
    )


__all__ = [
    "__version__",
    "apilevel",
    "threadsafety",
    "paramstyle",
    "connect",
    "Warning",
    "Error",
    "InterfaceError",
    "DatabaseError",
    "DataError",
    "OperationalError",
    "IntegrityError",
    "InternalError",
    "ProgrammingError",
    "NotSupportedError",
    "STRING",
    "BINARY",
    "NUMBER",
    "DATETIME",
    "ROWID",
    "Date",
    "Time",
    "Timestamp",
    "DateFromTicks",
    "TimeFromTicks",
    "TimestampFromTicks",
    "Binary",
]
