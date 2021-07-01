
from flask import Flask
from nltk.tokenize import word_tokenize

app = Flask(__name__)
@app.route('/')
def test():
    pass 


if __name__ == '__main__':
    test()
 
