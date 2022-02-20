from flask import Flask, render_template, redirect,request
import json
import firebase_admin
from firebase_admin import credentials, firestore
import random

cred = credentials.Certificate("revenue.json")
firebase_admin.initialize_app(cred)
store = firestore.client()


batch_lst = ['April2021','May2021','June2021','July2021','August2021','September2021','October2021','November2021','December2021','January2022','February2022','March2022']

app = Flask(__name__)


@app.route('/addstudents/<batch>', methods = ['GET','POST'])
def subjects(batch):
    dit = {}
    lst = []
    if request.method == "POST":
        dit = {}
        dit["name"] = request.form["name"]
        dit["contact"] = request.form["contact"]
        dit["email"] = request.form["email"]
        dit["age"] = int(request.form["age"])
        dit["program"], dit["amount"] = request.form["program"].split()
        dit["Batch"] = batch
        store.collection(dit["Batch"]).add(dit)
        store.collection(dit["program"]).add(dit)
        return redirect('/')

    dit["Batch"] = batch

    return render_template("student.html",stud = dit)



@app.route('/', methods = ['GET','POST'])
def addstudents():
    return render_template("index.html")



@app.route('/revenue',methods = ['GET','POST'])
def base():
    return render_template("base.html")

# @app.route('/createbatch', methods = ['GET','POST'])
# def batch():
#     for batch in batch_lst:
#         #print(batch)
#         docs = store.collection(batch).stream()
#         if docs:
#             for doc in docs:
#                 dit = {}
#                 dit = doc.to_dict()
#                 store.collection(dit["program"]).add(dit)
    
#     return redirect('/')


@app.route('/subject/<program>', methods = ['GET','POST'])
def subject(program):
    lst = []
    docs = store.collection(program).stream()
    for doc in docs:
        dit = {}
        dit["name"] = doc.to_dict().get("name")
        dit["subject_enrolled"] = doc.to_dict().get("program")
        lst.append(dit)


    return render_template("all.html", students = lst)


@app.route('/showrevenue', methods = ['GET','POST'])
def revenue():
    count=0
    revenue_lst = []
    for batch in batch_lst:
        #dit = {}
        lst = []
        sum1 = 0
        docs = store.collection(batch).stream()
        if docs:
            for doc in docs:
                sum1= sum1 + int(doc.to_dict().get("amount"))
                #print(sum1)
            #print(sum1)
            final_revenue = sum1
            #dit["batch"] = batch
            #lst.append(batch)
            #lst.append(final_revenue)
            revenue_lst.append(final_revenue)
            #revenue_lst.append(lst)
            #revenue_lst.append(dit)
        else:
            final_revenue = 0
            revenue_lst.append(final_revenue)
            #lst.append(batch)
            #lst.append(final_revenue)
            #dit[batch] = batch
            #revenue_lst.append(lst)
            #revenue_lst.append(dit)
        
        #revenue_dit = dict(revenue_lst)
        #print(type(revenue_lst))
    for batch in batch_lst:
        docs = store.collection(batch).stream()
        if docs:
            for doc in docs:
                count+=1
    
        
    
    return render_template("base.html",revenue = revenue_lst,number = count)



if __name__ == '__main__':
    app.run(host="127.0.0.1",port="4999",debug=True)
