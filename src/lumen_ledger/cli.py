"""Command line entry point for Lumen Ledger."""

import sys
from pathlib import Path

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
    if amount_cents == 0:
        click.echo("amount must be non-zero", err=True)
        sys.exit(2)
    entry = JournalEntry(account=account, amount_cents=amount_cents)
    click.echo(f"posted {entry.amount_cents} to {entry.account}")


def resolve_config_path(value):
    """Resolve a user supplied config path against the current directory."""
    return Path(value).expanduser().resolve()


@main.command("import")
@click.argument("path")
@click.option("--dry-run", is_flag=True, help="Validate the file without posting entries.")
def import_entries(path, dry_run):
    """Import journal entries from a CSV file."""
    click.echo(f"importing {path} (dry_run={dry_run})")


if __name__ == "__main__":
    sys.exit(main())
