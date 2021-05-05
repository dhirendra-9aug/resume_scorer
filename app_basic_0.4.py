# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:48:26 2021

@author: 91965
"""
import os
from sklearn import datasets

import pandas as pd
import functions
from flask import Flask, render_template, request , send_from_directory,redirect,url_for

__author__ = 'ibininja'

app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    df=pd.DataFrame()
    target = DOWNLOAD_FOLDER
    if not os.path.isdir(target):
        os.mkdir(target)

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
        print(df)   
        #destination = "/".join([target,df.name])
        df.to_csv(target+"df.csv")
    return redirect(url_for('uploaded_file', filename='df.csv'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
