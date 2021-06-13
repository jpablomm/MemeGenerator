import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote import QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   # './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    img_paths = next(os.walk(images_path))[2]
    imgs = [os.path.join(images_path, img_path) for img_path in img_paths]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    quote = QuoteModel(request.form['body'], request.form['author'])
    img_url = requests.get(request.form['image_url'])
    path_tmp = './tmp/image_temp.png'

    with open(path_tmp, 'wb') as tmp_img:
        tmp_img.write(img_url.content)

    path = meme.make_meme(path_tmp, quote.author, quote.body)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
