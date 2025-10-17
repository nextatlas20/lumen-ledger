"""Batch posting pipeline."""

from .ledger import JournalEntry


def post_batch(entries):
    """Post a batch of journal entries and return the number accepted."""
    valid = [entry for entry in entries if entry.amount_cents != 0]
    return len(valid)


def ensure_aware(timestamp):
    """Reject naive datetimes, which are ambiguous across DST boundaries."""
    if timestamp is not None and timestamp.tzinfo is None:
        raise ValueError("posted_at must be timezone-aware")
    return timestamp
