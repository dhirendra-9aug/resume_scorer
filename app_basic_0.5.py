# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:10:20 2021

@author: 91965
"""

import os
import pandas as pd
import functions
from flask import *

__author__ = 'ibininja'

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    df=pd.DataFrame()
    for file in request.files.getlist("file"):
        filename = file.filename
        if filename=="JD.PDF":
            a,b,c,d=functions.key_word_parser(file)
    for file in request.files.getlist("file"):
        filename = file.filename
        if filename!="JD.PDF":
           e,f,g,h=functions.key_word_parser(file)
           score=functions.compare_keywords(a, b, c, d, e, f, g, h)
           new_row = {'name':filename, 'score': score}
           df= df.append(new_row, ignore_index=True)   
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=scores.csv" 
    resp.headers["Content-Type"] = "text/csv"
    return resp




if __name__ == "__main__":
    app.run(debug=True)
