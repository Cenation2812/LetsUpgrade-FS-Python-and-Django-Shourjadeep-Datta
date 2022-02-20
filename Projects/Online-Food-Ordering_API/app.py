import firebase_admin
from firebase_admin import credentials,firestore
from flask import abort, jsonify, request
import flask
import json

cred = credentials.Certificate("Lets-food.json")
firebase_admin.initialize_app(cred)
store=firestore.client()

app=flask.Flask(__name__)


@app.route('/resto',methods=['POST'])
def addRESTAURANT():
    data=request.get_json(force=True)
    dit={}

    dit["name"]=data.get("name")
    dit["image"]=data.get("image")
    dit["location"]={"Lat":data.get("lat"),"long":data.get("lng")}
    dit["address"]=data.get("address")
    dit["Contact no"]=data.get("mobile")
    dit["type"]=data.get("tpe")

    store.collection("RESTAURANTS").add(dit)

    return jsonify("Success")

if __name__ == '__main__':
  app.run(host="127.0.0.1",port="5000",debug=False)

