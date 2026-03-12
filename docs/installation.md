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

