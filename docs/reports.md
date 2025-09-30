# Trial balance exports

`lumen_ledger.reports.trial_balance` aggregates journal entries into per-account balances.
Balances can be written out with `export_csv` or `export_parquet`.

```python
from lumen_ledger.reports import export_csv, trial_balance

export_csv(trial_balance(entries), "trial-balance.csv")
```

Parquet exports require the optional `pyarrow` extra.
