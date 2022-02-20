from flask import Flask, render_template, request,jsonify,redirect
import json
import time
import requests
import geopy
from geopy.geocoders import Nominatim
import random
from math import sin, cos, sqrt, atan2, radians
import beepy as beep
import firebase_admin
from firebase_admin import credentials, firestore


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("todo.json")
firebase_admin.initialize_app(cred)
store = firestore.client()


app = Flask(__name__)

@app.route('/home',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        dit = {}
        title = request.form["title"]
        desc = request.form["desc"]

        dit["title"] = title
        dit["desc"] = desc

        store.collection("TODOS").add(dit)
    todo_lst = []
    todos = store.collection("TODOS").stream()
    for doc in todos:
        d = {}
        d["id"] = doc.id
        d["title"] = doc.to_dict().get("title")
        d["desc"] = doc.to_dict().get("desc")
            
        todo_lst.append(d)
        #print(todo_lst)

    return render_template("base.html",todos = todo_lst)


@app.route('/update/<id>', methods = ['GET','POST'])
def update(id):
    print(id)
    if request.method == 'POST':
        print("post method")
        dit = {}
        dit["title"] = request.form["title"]
        dit["desc"] = request.form["desc"]
        print(id)
        store.collection("TODOS").document(id).set(dit)
    
    todo_lst = []
    doc = store.collection("TODOS").document(id).get()
    todo = doc.to_dict()
    todo["id"] = doc.id
    todo_lst.append(todo)

        
    return render_template("update.html", todo = todo)

@app.route('/delete/<id>', methods = ['GET','POST'])
def delete1(id):
    store.collection("TODOS").document(id).delete()
    return redirect('/home')


if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5001",debug=True)

