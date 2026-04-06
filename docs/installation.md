# Installation

## Python package

```bash
pip install pyaltibase
```

## Development install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## System prerequisites

- Python 3.10 or newer
- unixODBC or another compatible ODBC manager
- `pyodbc`
- An Altibase ODBC driver available to the runtime environment

## Connection styles

### Direct host and port

```python
import pyaltibase

conn = pyaltibase.connect(
    host="localhost",
    port=20300,
    database="mydb",
    user="sys",
    password="manager",
)
```

### DSN

```python
import pyaltibase

conn = pyaltibase.connect(dsn="ALTIBASE_TEST", user="sys", password="manager")
```

## Installation decision tree

```mermaid
flowchart TD
    A[Start setup] --> B{Python available?}
    B -->|No| C[Install supported Python]
    B -->|Yes| D[pip install pyaltibase]
    D --> E{pyodbc import works?}
    E -->|No| F[Install pyodbc and ODBC manager libs]
    E -->|Yes| G{Connection mode?}
    G -->|DSN| H[Configure DSN in ODBC manager]
    G -->|Driver| I[Install Altibase ODBC driver]
    H --> J[Test connect()]
    I --> J
```

!!! warning "ODBC dependency chain"
    `pyaltibase` needs both Python package dependencies and system ODBC pieces.
    Installing only `pyaltibase` is not enough if `pyodbc` or driver components are missing.

!!! info "DSN vs driver mode"
    - DSN mode centralizes connection attributes in ODBC manager.
    - Driver mode keeps host/port/driver directly in application code.

!!! tip "Connection checks"
    After installation, run a simple `SELECT 1` smoke test before integrating into larger services.
