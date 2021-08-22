# https://github.com/twtrubiks/Flask-Login-example

from flask import *
from flask_login import UserMixin, LoginManager
# from Model.dModel import *
from functools import wraps
import requests

app = Flask("Facebook Login App")
app.secret_key = 'hello facebook'  # Change this!
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message = "Please LOG IN"
login_manager.login_message_category = "info"

class User(UserMixin):
    pass

def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        get_fun = func(*args, **kwargs)
        return json.dumps(get_fun)

    return wrapper


@app.route('/login')
def login():
    return url_for("login")

# @app.route('/index', methods=['GET'])
@app.route('/')
def index():
    return url_for("index")

@app.route('/logout')
def logout():
    return url_for("index")

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
