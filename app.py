from flask import Flask
from flask import jsonify
from pprint import PrettyPrinter
import os, json
import db

app = Flask(__name__)
P = PrettyPrinter(indent=2)

def pretty(obj):
  P.pprint(obj)


def _response(data=None, status=200, error=None):
  return jsonify({
    'data': data,
    'status': status,
    'error': error
  })

@app.route('/')
def index():
  return _response(data='Hello World!')

@app.route('/user/<address>')
def user(address):
  user = db.get_user(address)
  if user:
    return _response(data=user)
  else:
    return _response(error='User not found', status=404)

@app.route('/prove_twitter/<address>')
def prove_twitter(address):
  user = db.get_user(address)
  if user:
    verified, handle = db.v_t(user)
    if verified:
      return _response(data=handle)
    else:
      return _response(error='Invalid Twitter proof', status=400)
  else:
    return _response(error='User not found', status=404)

if __name__ == '__main__':
  app.run()

