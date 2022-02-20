
from flask import Flask, render_template, request,jsonify,redirect
import json
import requests
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("banking.json")
firebase_admin.initialize_app(cred)
store = firestore.client()


app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def base():
    return render_template("base.html")

@app.route('/addcustomers',methods = ['GET','POST'])
def addcust():
    if request.method == 'POST':
        dit = {}
        dit["name"] = request.form["name"]
        dit["age"] = int(request.form["age"])
        dit["contact"] = request.form["contact"]
        dit["balance"] = int(request.form["balance"])
        dit["email"] = request.form["email"]
        dit["AccountCreatedAt"] = firestore.SERVER_TIMESTAMP

        store.collection("Customers").add(dit)
        return redirect('/')

    return render_template("add.html")


@app.route('/allcustomers', methods = ['GET','POST'])
def customers():
    docs = store.collection("Customers").stream()
    customer_lst = []
    for doc in docs:
        dit = {}
        dit["id"] = doc.id
        dit["name"] = doc.to_dict().get("name")
        # dit["age"] = doc.to_dict().get("age")
        # dit["contact"] = doc.to_dict().get("contact")
        # dit["balance"] = doc.to_dict().get("balance")
        customer_lst.append(dit)
    
    return render_template("show.html", customers =  customer_lst)

@app.route("/deleteaccount/<id>",methods = ['GET','POST'])
def deleteacc(id):
    store.collection("Customers").document(id).delete()
    return redirect('/allcustomers')

@app.route("/viewaccount/<id>",methods = ['GET','POST'])
def viewacc(id):
    doc = store.collection("Customers").document(id).get()
    d = {}
    #lst = []
    d = doc.to_dict()
    d["id"] = doc.id
    #lst.append(d)

    return render_template("view.html",users = d)


@app.route('/transaction',methods = ['GET','POST'])
def transact():
    docs = store.collection("Customers").stream()
    customer_lst = []
    for doc in docs:
        dit = {}
        dit["id"] = doc.id
        dit["name"] = doc.to_dict().get("name")
        # dit["age"] = doc.to_dict().get("age")
        # dit["contact"] = doc.to_dict().get("contact")
        # dit["balance"] = doc.to_dict().get("balance")
        customer_lst.append(dit)

    return render_template("tranx.html",customers = customer_lst)

@app.route('/tranx/<id>',methods = ['GET','POST'])
def trans(id):
    if request.method == 'POST':
        name = request.form["name"]
        amt = int(request.form["amt"])
        docs = store.collection("Customers").stream()
        for doc in docs:
            d = {}
            dit = {}
            if doc.to_dict().get("name") == name:
                dit["name"] = doc.to_dict().get("name")
                dit["age"] = doc.to_dict().get("age")
                c_id = doc.id
                dit["balance"] = doc.to_dict().get("balance") + amt
                store.collection("Customers").document(c_id).update(dit)
        doc = store.collection("Customers").document(id).get()
        if doc.to_dict().get("balance") > amt:
            dit = {}
            dit["balance"] = doc.to_dict().get("balance") - amt
            store.collection("Customers").document(id).update(dit)
            dit1 = {}
            dit1["sender"] = doc.to_dict().get("name")
            dit1["receiver"] = name
            dit1["Amount transacted"] = amt
            dit1["Transacted at"] = firestore.SERVER_TIMESTAMP
            store.collection("Transactions").add(dit1)

        return redirect('/allcustomers')



    doc = store.collection("Customers").document(id).get()
    d = {}
    d = doc.to_dict()
    d["id"] = id

    return render_template("maketransac.html",customer = d)
                

if __name__ == '__main__':
    app.run(host="127.0.0.1",port="5000",debug=True)