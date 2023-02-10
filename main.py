from flask import Flask, request

app = Flask(__name__)

@app.route("/home", methods=['GET'])
def hello():
   args = request.args
   name = args['name']

   return {'name': name}


if __name__ == "__main__":
   app.run(debug=True)
