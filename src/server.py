from flask import Flask
from flask import request
server = Flask(__name__)

@server.route("/search")

def search():
   message = request.args.get("message")
   for m in message:
      print(m)
   return message

if __name__ == "__main__":
   server.run(host='0.0.0.0')