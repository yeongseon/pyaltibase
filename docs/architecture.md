# Architecture

## Layers

1. Application code calls `pyaltibase.connect(...)`.
2. `pyaltibase.connection.Connection` builds an Altibase ODBC connection string.
3. `pyodbc` opens the real database connection.
4. `pyaltibase.cursor.Cursor` delegates execute and fetch operations to the native cursor.
5. Backend exceptions are mapped into package-owned DB-API exception classes.

## Design choices

- `qmark` parameter style matches `pyodbc` and DB-API 2.0 expectations.
- Package-owned exception classes keep the public API stable.
- Connection-string creation is isolated in `protocol.py` so backend behavior is testable.
- Unit tests use a fake `pyodbc` backend; e2e tests validate the real driver path.

## End-to-end runtime view

```mermaid
sequenceDiagram
    participant App as Application
    participant API as pyaltibase.connect
    participant Conn as Connection
    participant Proto as protocol.build_connection_string
    participant ODBC as pyodbc
    participant Cur as Cursor

    App->>API: connect(...)
    API->>Conn: create ConnectionConfig
    Conn->>Proto: build_connection_string(config)
    Proto-->>Conn: ODBC string
    Conn->>ODBC: connect(conn_str, autocommit, timeout)
    ODBC-->>Conn: native connection
    App->>Conn: cursor()
    Conn->>ODBC: native cursor()
    Conn-->>Cur: wrapped cursor
    App->>Cur: execute/fetch
```

## Error translation boundary

```mermaid
flowchart LR
    A[pyodbc Exception] --> B[_map_backend_error]
    B --> C[pyaltibase Error subclass]
    C --> D[Application catches stable public exceptions]
```

!!! note "Stability contract"
    Application code should catch `pyaltibase` exceptions, not backend-specific exceptions,
    to keep behavior stable when backend details evolve.

!!! tip "Extensibility"
    New connection attributes can be added without changing method signatures by routing through `**kwargs` into `ConnectionConfig.options`.
