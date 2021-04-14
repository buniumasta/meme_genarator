"""Helper module for test scenarios"""
from .quote_mode import QuoteMode

def get_csvfile_quotemode():
    """returns list of string quotemode objects as it is from CSVfile"""
    expected = [
        str(QuoteMode('Chase the mailman', 'Skittle')),
        str(QuoteMode('When in doubt, go shoe-shopping', 'Mr. Paws'))]
    return expected
