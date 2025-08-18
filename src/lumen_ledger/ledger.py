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
    return sum(entry.amount_cents for entry in entries if entry.amount_cents > 0)
