import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup

import re

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent

from flask import Flask
print(word_tokenize('word, two, three, four, five, six','one'))


def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

    
# https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/
output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',

]
def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output



def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext

html = epub2text('app/Redwall_books/Redwall.epub')
text = ''
for item in html:
    text += item

app = Flask(__name__)

@app.route('/')
def home():
    return text

if __name__ == '__main__':
    app.debug = True
    app.run()

# def api_response():
#     from flask import jsonify
#     if request.method == 'POST':
#         return jsonify(**request.json)