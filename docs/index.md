# pyaltibase

Unofficial Python DB-API 2.0 connector for Altibase.

## Key features

- Python DB-API 2.0-compatible interface for Altibase
- Direct host/port and DSN-based connection support
- Package-owned exception hierarchy and type constructors
- Docker-friendly testing workflow for unit and end-to-end coverage

## Quick install

```bash
pip install pyaltibase
```

## Quick connect example

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

## Documentation

- [Installation](installation.md)
- [Architecture](architecture.md)
- [Testing](testing.md)
- [Agent Playbook](agent-playbook.md)

## Project links

- [GitHub](https://github.com/yeongseon/pyaltibase)
- [PyPI](https://pypi.org/project/pyaltibase/)
- [Changelog](https://github.com/yeongseon/pyaltibase/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/yeongseon/pyaltibase/blob/main/CONTRIBUTING.md)

## Feature highlights

- DB-API 2.0 constants exported at module root (`apilevel`, `threadsafety`, `paramstyle`)
- Unified exception hierarchy independent from backend exception classes
- Connection-string assembly separated in protocol layer for testability
- Explicit connection controls for encoding (`nls_use`) and LOB compatibility (`long_data_compat`)

!!! info "Default connection values"
    `host="localhost"`, `port=20300`, and `user="sys"` are used unless you override them.

!!! tip "Prefer context managers"
    Using `with pyaltibase.connect(...) as conn:` ensures commit/rollback and close handling is consistent.

## How requests flow

```mermaid
flowchart LR
    A[Application] --> B[pyaltibase.connect]
    B --> C[ConnectionConfig]
    C --> D[build_connection_string]
    D --> E[pyodbc.connect]
    E --> F[Connection.cursor]
    F --> G[Cursor.execute/fetch]
    G --> H[Result tuples]
```

## Suggested reading path

1. [Installation](installation.md)
2. [Quick Start](quickstart.md)
3. [Connection Guide](connection.md)
4. [API Reference](api.md)
5. [Type Mapping](types.md)
6. [Error Handling](errors.md)
7. [FAQ](faq.md)
