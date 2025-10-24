"""Ledger entry primitives."""

from dataclasses import dataclass
from datetime import timezone


@dataclass
class JournalEntry:
    """A single debit or credit line."""

    account: str
    amount_cents: int
    currency: str = "USD"


def total_debits(entries):
    """Return the sum of all positive lines in a journal."""
    return sum(entry.amount_cents for entry in entries if entry.amount_cents > 0)


def dedupe_entries(entries):
    """Drop entries whose idempotency key was already seen in the batch."""
    seen = set()
    kept = []
    for entry in entries:
        key = getattr(entry, "idempotency_key", None)
        if key is not None and key in seen:
            continue
        if key is not None:
            seen.add(key)
        kept.append(entry)
    return kept


def as_utc(timestamp):
    """Return the timestamp normalised to UTC."""
    return timestamp.astimezone(timezone.utc)


_ACCOUNT_CACHE = {}


def canonical_account(name):
    """Return the canonical account name, memoising lookups."""
    if name not in _ACCOUNT_CACHE:
        _ACCOUNT_CACHE[name] = name.strip().lower()
    return _ACCOUNT_CACHE[name]
