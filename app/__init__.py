from ebooklib.utils import debug
from flask import Flask
from . import route
from .bookv2 import book_routes
import os

app = Flask(__name__)
app.config.update({"SECRET_KEY":os.environ.get("SECRET_KEY")})
# app.register_blueprint(route.bp)
app.register_blueprint(book_routes, url_prefix='/books')

if __name__ == '__main__':
    app.debug = True
    app.run()