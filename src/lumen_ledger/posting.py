"""Batch posting pipeline."""

from .ledger import JournalEntry


def post_batch(entries):
    """Post a batch of journal entries and return the number accepted."""
    valid = [entry for entry in entries if entry.amount_cents != 0]
    return len(valid)
