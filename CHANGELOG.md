# Changelog

All notable changes to Lumen Ledger are recorded in this file.
The format follows Keep a Changelog and the project adheres to Semantic Versioning.

## [Unreleased]

_No unreleased changes recorded._

## [2.4.0] - Unreleased

### Added

- **reports**: add trial balance export in CSV and Parquet
- **ledger**: require timezone-aware posting timestamps

### Changed

- **posting**: batch journal line validation with a single query
- **adapters**: extract retry policy into a shared helper
- **ledger**: cache account lookups for the posting loop

### Fixed

- **ledger**: serialise posting timestamps in UTC

### Removed

- Python 3.8 support is removed; the minimum supported version is 3.10

## [2.3.1] - 2025-09-12

### Fixed

- **cli**: exit with status 2 when the amount is zero
- **ledger**: reject duplicate idempotency keys on retry

## [2.3.0] - 2025-09-04

### Added

- **ledger**: support batch posting of journal entries
