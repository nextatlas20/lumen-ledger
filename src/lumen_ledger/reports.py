"""Trial balance exports."""

import csv
from pathlib import Path

from .ledger import JournalEntry


def trial_balance(entries):
    """Aggregate journal entries into per-account balances."""
    balances = {}
    for entry in entries:
        balances[entry.account] = balances.get(entry.account, 0) + entry.amount_cents
    return balances


def export_csv(balances, path):
    """Write balances to a CSV file with a stable account ordering."""
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["account", "balance_cents"])
        for account, balance in sorted(balances.items()):
            writer.writerow([account, balance])


def export_parquet(balances, path):
    """Write balances to a Parquet file."""
    import pyarrow as pa
    import pyarrow.parquet as pq

    table = pa.table(
        {
            "account": list(balances.keys()),
            "balance_cents": list(balances.values()),
        }
    )
    pq.write_table(table, path)
