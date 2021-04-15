"""
Meme Generator Functionality.

Extract data on near-Earth objects and close approaches from CSV and JSON.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""

import os
import random
from argparse import ArgumentParser
from quoteengine import Ingestor
from quoteengine import QuoteModel
from memegenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = ArgumentParser("Meme Generator - add caption to pictures")

    parser.add_argument(
        '--path',
        default=None,
        help='path to an image file')
    parser.add_argument(
        '--body',
        default=None,
        help='quote body to add to the image')
    parser.add_argument(
        '--author',
        default=None,
        help='quote author to add to the image')

    args = parser.parse_args()
    path_img = generate_meme(args.path, args.body, args.author)
    print(f"I've generated following file: {path_img}")
