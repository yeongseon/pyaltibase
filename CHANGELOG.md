# Changelog

## 0.2.0

- Added `_extract_backend_error_details` to preserve `errno` and `sqlstate` in mapped exceptions
- Mapped `DBAPIType` constants to real ODBC SQL type codes instead of placeholders
- Extended type system with `NUMBER` and `TIMESTAMP` variant mappings

## 0.1.0

- Added a DB-API 2.0 compatible package surface for Altibase
- Added a `pyodbc`-backed connection and cursor implementation
- Added Docker-based unit-test and e2e test workflows
- Added project documentation and development guides

