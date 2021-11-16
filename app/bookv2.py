#what is logging?
from logging import error

#Where do we use this?

#where?
import pandas as pd
#I used the ebooklib library in epub2thtml to extract the HTML out of the epub file using the “item.get_content()
import ebooklib
from ebooklib import epub
#BeautifulSoup provides a simple way to find text content (i.e. non-HTML) from the HTML and is used in chap2text
#https://medium.com/@zazazakaria18/turn-your-ebook-to-text-with-python-in-seconds-2a1e42804913
from bs4 import BeautifulSoup
#re is used in ...?
import re
# Flask is used in...?
# Blueprint is usd in...?
# request is used in...?
from flask import Flask, Blueprint, request
#string is used in...?
import string
#word_tokenize, sent_tokenize
from nltk.tokenize import word_tokenize, sent_tokenize
import os 

book_routes = Blueprint('bookv2', __name__)
pattern1 = re.compile("""[<span class="small">]*$""")

#epub2thml return chapters which is used in...
def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        
        if item.get_type() == ebooklib.ITEM_DOCUMENT and isinstance(item, ebooklib.epub.EpubHtml):
            chapters.append(item.get_content())
                # if (pattern1.findall((str(item.get_content()))))
            # if isinstance(item.get_content(), dict):
            #     print(item, 'this is a test')
            
    return chapters

# Now I will utilise the previous function to create another one that turns a list of HTML into a list of clean text
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

html = epub2text('app/Redwall_books/9_Redwall.epub')


# +++++++++++================= Routes ========================+++++++++++++++

@book_routes.route('/')
def home():
    # print(text)
    all_books = {}

    directory = r'app/Redwall_books'
    
    for file_name in os.listdir(directory):
        all_books[file_name] = file_name
    
    return all_books

# this route gives a particular book
@book_routes.route('/<book_title>')
def book_finder(book_title):
    book_title = book_title.lower()
    html = epub2text(f'app/Redwall_books/{book_title}.epub')

    my_book = {}
    count = 1
    for item in html:
        my_book[count] = item
        count += 1
    return my_book

# this route give a cetain page/chapter/section
@book_routes.route('<book_title>/<int:my_page>')
def word_count(my_page, book_title):
    book_title = book_title.lower()
    print(my_page, 'test')
    html = epub2text(f'app/Redwall_books/{book_title}.epub')

    my_book = {}
    count = 1
    for item in html:
        my_book[count] = item
        count += 1
    return my_book[my_page]



# this route give you a certain number of words

@book_routes.route('/<book_name>/<int:chapter>/<int:words>')
def example(book_name, chapter, words):
    book_title = book_name.lower()
    html = epub2text(f'app/Redwall_books/{book_title}.epub')
    
    my_book = {}
    
    count = 1
    for item in html:
        my_book[count] = item
        count += 1

    my_chapter = my_book[chapter]
    print(type(my_chapter))
  
    my_list = my_chapter.split(' ')
    selected_words = my_list[0:words]
    return ' '.join(selected_words)


# def api_response():
#     from flask import jsonify
#     if request.method == 'POST':
#         return jsonify(**request.json)