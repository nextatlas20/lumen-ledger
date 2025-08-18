"""Command line entry point for Lumen Ledger."""

import sys

import click

from .ledger import JournalEntry


@click.group()
def main():
    """Lumen Ledger command line tools."""


@main.command("post")
@click.argument("account")
@click.argument("amount_cents", type=int)
def post(account, amount_cents):
    """Post a single journal entry."""
    entry = JournalEntry(account=account, amount_cents=amount_cents)
    click.echo(f"posted {entry.amount_cents} to {entry.account}")


if __name__ == "__main__":
    sys.exit(main())
