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
