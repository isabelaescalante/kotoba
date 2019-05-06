#!flask/bin/python
from flask import Flask
from flask import jsonify, json
from flask import make_response
from flask import request
from flask import abort
from flask_cors import CORS, cross_origin
import flask

import numpy as np

import sys
sys.path.insert(0,'..')

import main

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET'])
def test() :
    print ("ENTRO A TEST")
    return "hello world"

@app.route('/parse', methods=['POST'])
def arguments() :
    print ("ENTRO A ARGUMENT")
    if not request.json:
        print ("RESULT CODE")
        result_code = 400
    else:
        print ("000")
        f = request.json['f']
        result = f+a+b+n

    return jsonify({'result': result}), 201

if __name__ == '__main__':
    #print flask.__version__
    app.run(debug=True)
