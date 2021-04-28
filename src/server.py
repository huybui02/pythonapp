from flask import Flask
from flask import request
server = Flask(__name__)

@server.route("/search")

def search():
   result = ""
   string = request.args.get("message")
   count = 1
   result += string[0]

   for i in range(len(string)-1):
      if(string[i] == string[i+1]):
         count+=1
      else:
         if(count > 1):
               result += str(count)
         result += string[i+1]
         count = 1
   if(count > 1):
      result += str(count)
   return result

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=8080)