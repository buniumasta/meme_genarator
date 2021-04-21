"""Helper module for test scenarios."""
from .quote_model import QuoteModel


def get_csvfile_art():
    """Return list of string quotemode objects as it is from CSVfile."""
    expected = [
        str(QuoteModel('Every artist was first an amateur',
                       'Ralph Waldo Emerson')),
        str(QuoteModel('Creativity takes courage', 'Henri Matisse')),
        str(QuoteModel('Every child is an artist. '
                       'The problem is how to remain '
                       'an artist once we grow up', 'Pablo Picasso')),
        str(QuoteModel('You don’t take a photograph - '
                       'you make it', 'Ansel Adams')),
        str(QuoteModel('Art enables us to find ourselves '
                       'and lose ourselves at the same time',
                       'Thomas Merton')),
        str(QuoteModel('We don’t make mistakes - '
                       'just happy little accidents', 'Bob Ross')),
        str(QuoteModel('Have no fear of perfection - '
                       'you’ll never reach it', 'Salvador Dali')),
        str(QuoteModel('You can’t wait for inspiration - '
                       'you have to go after it with a club', 'Jack London'))]
    return expected


def get_csvfile_dog():
    """Return list of string quotemode objects as it is from CSVfile."""
    expected = [
        str(QuoteModel('Chase the mailman', 'Skittle')),
        str(QuoteModel('When in doubt, go shoe-shopping', 'Mr. Paws'))]
    return expected


def get_docxfile_dog():
    """Return list of string quotemode objects as it is from DOCXfile."""
    expected = [
        str(QuoteModel('"Bark like no one’s listening"', 'Rex')),
        str(QuoteModel('"RAWRGWAWGGR"', 'Chewy')),
        str(QuoteModel('"Life is like peanut butter: crunchy"', 'Peanut')),
        str(QuoteModel('"Channel your inner husky"', 'Tiny'))]
    return expected


def get_txtfile_dog():
    """Return list of string quotemode objects as it is from TXTfile."""
    expected = [
        str(QuoteModel('To bork or not to bork', 'Bork')),
        str(QuoteModel('He who smelt it...', 'Stinky'))]
    return expected


def get_pdffile_dog():
    """Return list of string quotemode objects as it is from PDFfile."""
    expected = [
        str(QuoteModel('"Treat yo self"', 'Fluffles')),
        str(QuoteModel('"Life is like a box of treats"', 'Forrest Pup')),
        str(QuoteModel(
            "\"It's the size of the fight in the dog\"",
            'Bark Twain'))
        ]
    return expected
