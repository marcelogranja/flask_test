#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:09:57 2018

@author: mgn
"""


from flask import Flask, jsonify, request
import pickle

with open('model.pck', 'rb') as fp:
    scaler, model = pickle.load(fp )

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json()
    
    # parsers json
    
    error_msg = {}
    x = []
    for key in ['x1','x2','x3']:
        try:

            value = payload[key]       
            value = float(value)            
            x.append( value )
            
        except KeyError: # if variable is not present
           error_msg[key] = key + ' is missing'
           
        except ValueError: # if variable content is not valid
           error_msg[key] = key + ' should be a number'
            
    # if input data is not valid, returns 422 error
    if len(error_msg) > 0:
        return jsonify(error_msg), 422

    x_scaled = scaler.transform([x])
    y = model.predict(x_scaled)[0]
    
    return jsonify({'y': y}), 200


if __name__ == '__main__':    
    app.run(debug=False)
    