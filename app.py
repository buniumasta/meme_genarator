"""
Web Flask Application generating meme on pictures.

Extract data on quote_model objects from CSV, Doc, PDF and JSON files.
Then exctracted data (author & quote) are placed randomly on pictures.

Web application uses quoteengine and memegenerator modules.
"""
import random
import os
from shutil import copyfileobj
import requests
from flask import Flask, render_template, abort, request, send_file
from PIL import UnidentifiedImageError
from quoteengine import Ingestor
from quoteengine import QuoteModel
from memegenerator import MemeEngine
from memegenerator import gen_ppt


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/ArtQuotes/ArtQuotesTXT.txt',
                   './_data/ArtQuotes/ArtQuotesDOCX.docx',
                   './_data/ArtQuotes/ArtQuotesPDF.pdf',
                   './_data/ArtQuotes/ArtQuotesCSV.csv']

    quotes_list = []

    for quote_file in quote_files:
        quote_list_tmp = Ingestor.parse(quote_file)
        if quote_list_tmp is not None:
            quotes_list.extend(quote_list_tmp)

    print(quotes_list)
    print(f'I have following number of quots {len(quotes_list)}')
    images_path = "./_data/photos/art/"

    for root, _, files in os.walk(images_path):
        images = [os.path.join(root, name) for name in files]

    if len(images) > 0:
        img = random.choice(images)
        print(img)
    else:
        raise FileNotFoundError("I cannot find any images")

    if len(quotes_list) > 0:
        quote = random.choice(quotes_list)
        print(quote)
    else:
        raise FileNotFoundError("I cannot find any quotes")
    return quote, img


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    try:
        quote, img = setup()

        path = meme.make_meme(img, quote.body, quote.author)
        pathppt = gen_ppt(path, quote.body)
        return render_template('meme.html', path=path, pathppt=pathppt)

    except FileNotFoundError as exc:
        quote = QuoteModel("We couldn't open files", "Admin")
        mymeme = MemeEngine('./static')
        img = './_data/photos/broken/pexels-pixabay-209235.jpeg'
        path = mymeme.make_meme(img, quote.body, quote.author)
        print(exc)
        return render_template('meme.html', path=path, pathppt=pathppt)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    try:
        img = download_image(image_url)
        if img:
            quote = QuoteModel(body, author)
            mymeme = MemeEngine('./static')
            path = mymeme.make_meme(img, quote.body, quote.author)
            pathppt = gen_ppt(path, quote.body)

            # 3. Remove the temporary saved image.
            os.remove(img)

    except (requests.exceptions.ConnectionError,
            FileNotFoundError,
            UnidentifiedImageError
            ) as exc:
        quote = QuoteModel("We couldn't download"
                           " an image from provided URL", "Admin")
        mymeme = MemeEngine('./static')
        img = './_data/photos/broken/pexels-pixabay-209235.jpeg'
        path = mymeme.make_meme(img, quote.body, quote.author)
        print(exc)

    return render_template('meme.html', path=path, pathppt=pathppt)


def download_image(image_url: str):
    """Download image from Internet."""
    filename = './static/' + image_url.split("/")[-1]
    req_image = requests.get(image_url, stream=True)

    if req_image.status_code == 200:
        req_image.raw.decode_content = True

        with open(filename, 'wb') as file:
            copyfileobj(req_image.raw, file)
        print('Image sucessfully Downloaded: ', filename)
        return filename
    print('Image Couldn\'t be retreived')
    raise FileNotFoundError('Image could be downloaded')


if __name__ == "__main__":
    app.run()
