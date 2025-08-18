from lumen_ledger.ledger import JournalEntry, total_debits


def test_total_debits_sums_positive_amounts():
    entries = [JournalEntry("cash", 500), JournalEntry("fees", -120)]
    assert total_debits(entries) == 500
