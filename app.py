####### Simple Flask ######
#!/user/bin/python
__author__ = "Midhunkumar"
__version__ = "1.0.1"
__status__ = "DEV"
#############################

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods =["GET","POST","COPY","PUT"])
def home():
  if request.method == "GET":
      return "This is GET Request"
  elif request.method == "POST":
       return "This is POST Method"
  else :
      return "this is " + request.method + " Method"


    
if __name__ == "__main__":
    app.run(debug=True)