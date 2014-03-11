#
import flask

app = flask.Flask(__name__)
from views import all

if __name__ == '__main__':
    app.run()

