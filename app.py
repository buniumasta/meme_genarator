"""
Web Flask Application generating meme on pictures.

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
import random
import os
import requests
from flask import Flask, render_template, abort, request
from quoteengine import Ingestor
from memegenerator import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes_list = []

    for quote_file in quote_files:
        quote_list_tmp = Ingestor.parse(quote_file)
        if quote_list_tmp is not None:
            quotes_list.extend(quote_list_tmp)

    images_path = "./_data/photos/dog/"

    for root, _, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]

    img = random.choice(images)
    print(img)
    quote = random.choice(quotes_list)
    print(quote)
    return quote, img

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    quote, img = setup()

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
