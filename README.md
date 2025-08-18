# Lumen Ledger

Double-entry ledger service for the Lumen billing platform.

## Layout

- `src/lumen_ledger/` – posting engine, reporting helpers and the CLI
- `tests/` – pytest suite
- `docs/` – operator documentation

## Development

```bash
uv sync --extra dev
uv run pytest
```
