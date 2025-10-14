from lumen_ledger.ledger import JournalEntry
from lumen_ledger.reports import trial_balance


def test_trial_balance_groups_by_account():
    entries = [JournalEntry("cash", 300), JournalEntry("cash", -100), JournalEntry("fees", 25)]
    assert trial_balance(entries) == {"cash": 200, "fees": 25}


def test_trial_balance_of_empty_journal():
    assert trial_balance([]) == {}
