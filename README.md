# pyaltibase

[![CI](https://github.com/yeongseon/pyaltibase/actions/workflows/ci.yml/badge.svg)](https://github.com/yeongseon/pyaltibase/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/pyaltibase)](https://pypi.org/project/pyaltibase/)
[![docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://yeongseon.github.io/pyaltibase/)

**Unofficial Python DB-API 2.0 connector for Altibase**

`pyaltibase` provides a Pythonic DB-API 2.0 interface for Altibase databases.
The current implementation uses `pyodbc` as the transport backend and wraps
Altibase ODBC connectivity behind a clean, package-owned API surface.

This is an independent community project and is not officially supported by
Altibase Corporation. This project is not affiliated with Altibase Corporation.

## Why pyaltibase

- Python DB-API 2.0 compatible module surface
- Direct host/port or DSN-based Altibase ODBC connections
- Package-owned exception hierarchy and type constructors with `errno`/`sqlstate` preservation
- Dockerized unit-test workflow with a 95% coverage target
- Docker-based end-to-end test harness for licensed Altibase environments

## Installation

### Python package

```bash
pip install pyaltibase
```

### System requirements

- Python 3.10+
- `pyodbc`
- unixODBC or an equivalent ODBC manager
- An Altibase ODBC driver installed on the host or in the container

## Quick Start

```python
import pyaltibase

with pyaltibase.connect(
    host="localhost",
    port=20300,
    database="test",
    user="sys",
    password="manager",
) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print(cursor.fetchall())
```

### DSN connection

```python
import pyaltibase

conn = pyaltibase.connect(dsn="ALTIBASE_TEST", user="sys", password="manager")
```

## Testing

### Unit tests in Docker

```bash
make test-docker
```

This runs the package test suite inside Docker and enforces a `95%` coverage
threshold.

### End-to-end tests in Docker

```bash
make test-e2e-docker
```

The e2e flow expects a licensed Altibase Docker image. See
[docs/testing.md](docs/testing.md) for the required environment variables.

## Documentation

- [docs/README.md](docs/README.md)
- [docs/installation.md](docs/installation.md)
- [docs/testing.md](docs/testing.md)
- [docs/architecture.md](docs/architecture.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

## Project Layout

```text
pyaltibase/
    __init__.py
    connection.py
    cursor.py
    exceptions.py
    types.py
    protocol.py
    config.py
tests/
docs/
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
