from lumen_ledger.ledger import JournalEntry, total_debits


def test_total_debits_sums_positive_amounts():
    entries = [JournalEntry("cash", 500), JournalEntry("fees", -120)]
    assert total_debits(entries) == 500


def test_post_batch_skips_zero_amounts():
    from lumen_ledger.posting import post_batch

    entries = [JournalEntry("cash", 0), JournalEntry("cash", 250)]
    assert post_batch(entries) == 1


def test_dedupe_entries_drops_repeated_keys():
    from lumen_ledger.ledger import dedupe_entries

    entries = [JournalEntry("cash", 100), JournalEntry("cash", 100)]
    entries[0].idempotency_key = "k-1"
    entries[1].idempotency_key = "k-1"
    assert len(dedupe_entries(entries)) == 1
