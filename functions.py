# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:45:15 2021

@author: 91965
"""
import PyPDF2
import pandas as pd
keywords=pd.read_csv("keywords.csv",encoding = 'unicode_escape')
keywords.columns
skills=list(keywords['Skills'].dropna())
tools=list(keywords['tools/languages'].dropna())
libraries=list(keywords['libraries'].dropna())
algo=list(keywords['ML Algorithms'].dropna())

def key_word_parser(file):
    jd=PyPDF2.PdfFileReader(file.stream)
    jd2=""
    for i in  range(jd.getNumPages()):
        jd2+= jd.getPage(i).extractText() 
        
    jd2=jd2.split()  
    jd2 = [each_string.lower() for each_string in jd2]
    jd2 = [each_string.replace(",","") for each_string in jd2]
    a=set(jd2).intersection(tools)
    b=set(jd2).intersection(skills)
    c=set(jd2).intersection(libraries)
    d=set(jd2).intersection(algo)
    return a,b,c,d
def compare_keywords(a,b,c,d,e,f,g,h):
    w=set(a).intersection(e)
    x=set(b).intersection(f)
    y=set(c).intersection(g)
    z=set(d).intersection(h)
    score = (len(w)+len(x)+len(y)+len(z))/(len(a)+len(b)+len(c)+len(d))*100
    return score       





