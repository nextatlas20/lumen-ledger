"""Batch posting pipeline."""

from .ledger import JournalEntry


def post_batch(entries):
    """Post a batch of journal entries and return the number accepted."""
    accepted = 0
    for entry in entries:
        if entry.amount_cents == 0:
            continue
        accepted += 1
    return accepted
