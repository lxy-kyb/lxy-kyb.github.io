# -*- coding: utf-8 -*-
from flask import Flask,render_template,send_from_directory
import json
import time
import os
import codecs
import shelve

app = Flask(__name__)

@app.route('/')
def user():
    return render_template('index.html')

@app.route('/Articles/<page>')
def Articles(page):
    return send_from_directory('Articles', page)

@app.route('/Pages/<current>')
def userIndex(current):
    global maxp, maxcap
    global dict_Artcles
    Sindex = [];
    Eindex = [];
    current = str(current).split('.')[0]
    num = int(current)
    urlstr = '/Pages/{0}.html'
    if maxp <= 17:    
        for i in range(1,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    elif num <= 9:
        for i in range(1,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxcap - 3):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
        Eindex.append({'url': str.format(urlstr, num+5) ,'tags': '...' })
        for i in range(maxp-2,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    elif num <= maxp-8:
        for i in range(1,4):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        Sindex.append({'url': str.format(urlstr, num-5) ,'tags': '...' })
        for i in range(num-4,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,num+5):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
        Eindex.append({'url': str.format(urlstr, num+5) ,'tags': '...' })
        for i in range(maxp-2,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    else:
        for i in range(1,4):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        Sindex.append({'url': str.format(urlstr, num-5) ,'tags': '...' })
        for i in range(maxp-maxcap + 5,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    prepage = str.format(urlstr, num if num == 1 else num-1)
    nextpage= str.format(urlstr, num if num == maxp else num + 1)
    currentdata  = []
    if num <= maxp:
        for lst in range((num-1)*10, min((num-1)*10 + 10, len(dict_Artcles))):            
            currentdata.append(dict_Artcles.items()[lst][1]);   
        return render_template('articlelist_base.html',Sindex = Sindex, current = num,Eindex = Eindex,PP = prepage, NP = nextpage, Content = currentdata)

def GetRange(dtlist, start, len):
    newlist = []
    for i in range(start, start + len):
        newlist.append(dtlist[i])

def Init():
    global dict_Artcles
    with codecs.open('index.json') as file:
        jsonCode = file.read()    
    dict_Artcles = json.loads(jsonCode)
    global maxp 
    global maxcap
    maxp = len(dict_Artcles)/10 + 1
    maxcap = 17

INDEX_DAT = 'index.dat'
if __name__ == '__main__':
    Init()
    app.run(debug=True)