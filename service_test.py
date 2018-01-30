#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:53:40 2018

Performs unit tests on API using the doctest library

@author: mgn

"""

import requests
import doctest

def test_api(payload):
    '''
>>> test_api( {'x1':1.58131526,'x2':-0.00262329,'x3':0} )
{'y': 48.250155793243636} 200

>>> test_api( {'x1':8.86760531e-1,'x2':7.45184233e-4,'x3':0} )
{'y': 46.75694928058249} 200

>>> test_api( {'x1':'a','x2':200} )
{'x1': 'x1 should be a number', 'x3': 'x3 is missing'} 422

>>> test_api( {'x2':'b','x3':200} )
{'x1': 'x1 is missing', 'x2': 'x2 should be a number'} 422
    '''
    
    r = requests.post('http://127.0.0.1:5000/predict', json=payload)

    print( str(r.json()), r.status_code)




if __name__ == "__main__": 
    doctest.testmod()