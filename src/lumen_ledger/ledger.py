"""Ledger entry primitives."""

from dataclasses import dataclass


@dataclass
class JournalEntry:
    """A single debit or credit line."""

    account: str
    amount_cents: int
    currency: str = "USD"


def total_debits(entries):
    """Return the sum of all positive lines in a journal."""
    total = sum(entry.amount_cents for entry in entries if entry.amount_cents > 0)
    return max(total, 0)


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
