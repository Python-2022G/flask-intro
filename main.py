from flask import Flask, request
import requests


app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
   
   return "ok"


@app.route("/home", methods=['GET'])
def hello():
   args = request.args
   name = args['name']

   return {'name': name}


@app.route('/bot', methods=["POST"])
def bot():
   if request.method == "POST":
      data = request.get_json()

      print(data)


      return {"message": "ok"}
