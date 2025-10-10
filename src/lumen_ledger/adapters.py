"""Shared retry policy for outbound adapters."""

import time

DEFAULT_ATTEMPTS = 3
DEFAULT_DELAY_SECONDS = 0.5


def with_retries(call, attempts=DEFAULT_ATTEMPTS):
    """Call ``call`` up to ``attempts`` times with linear backoff."""
    last_error = None
    for attempt in range(1, attempts + 1):
        try:
            return call()
        except Exception as error:  # noqa: BLE001 - re-raised after the final attempt
            last_error = error
            if attempt < attempts:
                time.sleep(DEFAULT_DELAY_SECONDS * attempt)
    raise last_error
