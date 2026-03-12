# Testing

## Unit tests

Unit tests run in Docker and enforce at least `95%` line coverage.

```bash
make test-docker
```

The unit-test container installs development dependencies and runs:

```bash
python -m pytest --cov=pyaltibase --cov-report=term-missing --cov-fail-under=95
```

## End-to-end tests

End-to-end tests are Docker-based and expect an Altibase Docker image with the
required runtime and license setup available.

### Required environment variables

- `ALTIBASE_IMAGE` (optional, defaults to `altibase/altibase:latest`)
- `ALTIBASE_PORT` (optional, defaults to `20300`)
- `ALTIBASE_DATABASE` (optional)
- `ALTIBASE_USER` (optional)
- `ALTIBASE_PASSWORD` (optional)
- `ALTIBASE_DRIVER` (optional)
- `ALTIBASE_NLS_USE` (optional)

### Run e2e

```bash
make test-e2e-docker
```

The e2e test runner waits for the database port and then runs the package smoke
tests against the live service.

