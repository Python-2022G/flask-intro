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

      chat_id = data['message']['chat']['id']

      url = 'https://api.telegram.org/bot6217675093:AAFKzEEhkFi-nQqkrk7LTyyBgIyww7d8UtQ/sendMessage'
      payload = {
         "chat_id": chat_id,
         'text': 'salom'
      }

      requests.get(url, params=payload)


      return {"message": "ok"}
