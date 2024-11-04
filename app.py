from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return 


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/registro")
def registro():
    return "Hola soy el registro"


app.run(host="0.0.0.0", port=5001, debug=True)