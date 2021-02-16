# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:26:10 2021

@author: mshahzamal
"""

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

#naming our app as app
app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
