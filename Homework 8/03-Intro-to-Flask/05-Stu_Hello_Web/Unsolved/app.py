
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("Server received request for 'Index' page...")
    return "Welcome to my API Index"

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my About Page"

@app.route("/contact")
def contact(): 
    print ("Server received request for 'Index' page...")
    return "Welcome to my contact page. Call me for a good time. XOXO"

if __name__ == "__main__":
    app.run(debug=True)
    