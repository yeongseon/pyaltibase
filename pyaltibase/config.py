"""Configuration primitives for pyaltibase."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ConnectionConfig:
    """Connection settings accepted by :func:`pyaltibase.connect`."""

    host: str = "localhost"
    port: int = 20300
    database: str = ""
    user: str = "sys"
    password: str = ""
    dsn: str | None = None
    driver: str = "ALTIBASE_HDB_ODBC_64bit"
    autocommit: bool = False
    login_timeout: int | None = None
    nls_use: str | None = None
    long_data_compat: bool = True
    options: dict[str, object] = field(default_factory=dict)
