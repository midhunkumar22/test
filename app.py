from flask import Flask, request


app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def home():
  if request.method == "GET":
      return "This is GET Request"
  elif request.method == "POST":
       return "This is POST Method"
  else :
      return "this is " + request.method + "method"


    
if __name__ == "__main__":
    app.run(debug=True)