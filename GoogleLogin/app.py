# https://www.youtube.com/watch?v=FKgJEfrhU1E

from os import abort

from flask import Flask, session

app = Flask("google login app")
app.secret_key = "CodeSpecialist.com"

def login_is_required(funtion):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else:
            return funtion()
    return wrapper()

@app.route("/login")
def login():
    pass

@app.route("/callback")
def callback():
    pass

@app.route("/logout")
def logout():
    pass

@app.route("/")
def index():
    return "Hello Google Login"

@app.route("/protected_area")
def protected_area():
    pass

if __name__ == "__main__":
    app.run(debug=True)