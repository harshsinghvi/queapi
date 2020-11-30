import flask 
import json 
import os
from flask_pymongo import PyMongo
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask import render_template
import creds
from que import Que

def get_que_from_db():
    quedb=mongo.db.que.find({"name" :"que0"})[0]
    que._que['data'] = quedb['data']
    que._data_validate()
    return "OK",200

def dbupdate():
    temp={
        "$set":{
        "data":que.que(),
        "size":que.size()
        }
    }
    try :
        mongo.db.que.update_one({"name":"que0"},temp)
    except: 
        return "Internal Server Error With DB", 500
    return "DB UPDATE OK",200

#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = False
MONGO_DB_URI = os.environ['MONGO_DB_URI']
app.config['MONGO_URI'] = MONGO_DB_URI
mongo = PyMongo(app)
quedb=mongo.db.que.find({"name" :"que0"})[0]
que = Que(elements=quedb['data'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/que',methods=['GET'])
def view_que():
    get_que_from_db()
    return json.dumps(que.raw_que()),200

@app.route('/get',methods=['GET'])
def get():
    que.get()
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"GET":"OK"},200

@app.route('/put',methods=['GET'])
def put():
    if 'data' not in request.args:
        return "Bad Request Please Pass the data in the Quary Parameters",400
    que.put(request.args['data'])
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"PUT":" OK"},200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
