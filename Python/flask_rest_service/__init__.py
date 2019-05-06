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

@app.route('/arguments', methods=['POST'])
def arguments() :
    print ("ENTRO A ARGUMENT")
    if not request.json:
        print ("RESULT CODE")
        result_code = 400
    else:
        print ("000")
        f = request.json['f']
        a = request.json['a']
        b = request.json['b']
        n = request.json['n']
        result = f+a+b+n

    return jsonify({'result': result}), 201



@app.route('/simpsons', methods=['POST'])
def simpsons() :
    if not request.json:
        result_code = 400
    else:
        f = str(request.json['f'])
        a = float(request.json['a'])
        b = float(request.json['b'])
        n = float(request.json['n'])
        result = simpson_simple(f,b,a,n)

    return jsonify({'result': result}), 201

@app.route('/lagrangei', methods=['POST'])
def lagrangei() :
    if not request.json:
        result_code = 400
    else:
        x = request.json['x']
        y = request.json['y']
        x_int = float(request.json['xint'])
        x_array = map(float, x.split(','))
        #print x_array
        y_array = map(float, y.split(','))
        #print y_array
        result = lagrange(x_array,y_array, x_int)
        #print result

    return jsonify({'result': result}), 201

@app.route('/gauss', methods=['POST'])
def gauss() :
    if not request.json:
        result_code = 400
    else:
        data = request.json
        value = data.get('f')
        result = solve_sistema(value)
    return jsonify({'result': result}), 201

@app.route('/montante', methods=['POST'])
def montante() :
    if not request.json:
        result_code = 400
    else:
        data = request.json
        value = data.get('f')
        result = solve_sistema(value)

    return jsonify({'result': result}), 201

@app.route('/biseccions', methods=['POST'])
def biseccions() :
    if not request.json:
        result_code = 400
    else:
        f = str(request.json['f'])
        a = float(request.json['a'])
        b = float(request.json['b'])
        tol = float(request.json['tol'])
        iterm = float(request.json['iterm'])

        result = biseccion(f, a, b, tol, iterm)

    return jsonify({'result': result}), 201

@app.route('/newtonrap', methods=['POST'])
def newtonrap() :
    if not request.json:
        result_code = 400
    else:
        f = str(request.json['f'])
        df = str(request.json['df'])
        xcero = float(request.json['x0'])
        tol = float(request.json['tol'])
        iterm = int(request.json['iterm'])

        result = newtonRapson(f, df, xcero, tol, iterm)
        #print result

    return jsonify({'result': result}), 201

@app.route('/aExponencial', methods=['POST'])
def aExponencial() :
    if not request.json:
        result_code = 400
    else:
        x = str(request.json['x'])
        y = str(request.json['y'])
        #print x_array
        #print y_array
        result = exponencial(x,y)
        #print result

    return jsonify({'result': result}), 201

@app.route('/aPolinomial', methods=['POST'])
def aPolinomial() :
    if not request.json:
        result_code = 400
    else:
        x = str(request.json['x'])
        y = str(request.json['y'])
        n = float(request.json['orden'])
        #print x_array
        #print y_array
        result = polinomial(x,y,n)
        #print result

    return jsonify({'result': result}), 201

if __name__ == '__main__':
    #print flask.__version__
    app.run(debug=True)
