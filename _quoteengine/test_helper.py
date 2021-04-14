"""Helper module for test scenarios."""
from .quote_model import QuoteModel


def get_csvfile_quotemode():
    """Return list of string quotemode objects as it is from CSVfile."""
    expected = [
        str(QuoteModel('Chase the mailman', 'Skittle')),
        str(QuoteModel('When in doubt, go shoe-shopping', 'Mr. Paws'))]
    return expected
