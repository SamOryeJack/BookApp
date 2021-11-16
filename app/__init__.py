from ebooklib.utils import debug
from flask import Flask, request, redirect
from flask.config import Config
from werkzeug.utils import redirect
from flask_cors import CORS

from . import route
from .bookv2 import book_routes
import os
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
# app.register_blueprint(route.bp)
app.register_blueprint(book_routes, url_prefix='/books')

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

if __name__ == '__main__':
    app.debug = True
    app.run()