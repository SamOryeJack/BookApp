from ebooklib.utils import debug
from flask import Flask
from . import route
import os

app = Flask(__name__)
app.config.update({"SECRET_KEY":os.environ.get("SECRET_KEY")})
app.register_blueprint(route.bp)

if __name__ == '__main__':
    app.run(debug = True)