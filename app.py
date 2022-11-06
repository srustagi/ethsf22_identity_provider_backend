from flask import Flask
from flask import jsonify
from pprint import PrettyPrinter
import os, json

app = Flask(__name__)
P = PrettyPrinter(indent=2)

def pretty(obj):
  P.pprint(obj)


def env(var):
  return os.environ.get(var)

def _response(status=200, message='', error=None):
  return jsonify({
    'status': status,
    'message': message,
    'error': error
  })



@app.route('/')
def index():
  return _response(message='Hello World!')

if __name__ == '__main__':
  app.run()

