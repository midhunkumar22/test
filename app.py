from flask import Flask

app = Flask(__name__)

@app.route("/", methods =["GET"])
def home():
    return "Hello, World!"
@app.route("/", methods =["POST"])   
def End():
    return "Bye, World!"
    
if __name__ == "__main__":
    app.run(debug=True)