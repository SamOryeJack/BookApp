from flask import Flask
from flask import Blueprint
import re

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('app/Redwall_books/9_Redwall.epub')

bp = Blueprint("books", __name__, url_prefix='/books')
@bp.route("/")
def homepage():
    return 'Hello'


