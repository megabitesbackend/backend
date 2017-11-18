"""BLOCK PARTY Server File"""

# from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request,
                   flash, session, abort, url_for)
from flask_debugtoolbar import DebugToolbarExtension

#libraries for API requests
from sys import argv
from pprint import pprint, pformat

from model import db, connect_to_db, Donor, Address, Receiver, Food

# from passlib.hash import bcrypt

# from flask_login import LoginManager, login_user, login_required, logout_user, current_user 
import os
from datetime import datetime
from sqlalchemy import and_


app = Flask(__name__)
app.secret_key = "ABC"


# Raises an error in Jinja
# app.jinja_env.undefined = StrictUndefined

######################################
#For Registration and Login
######################################

# login_manager = LoginManager()
# login_manager.init_app(app)

# login_manager.login_view = 'render_login_page'


@app.route('/')
def index():
    """Homepage with map."""

    return render_template("map.html")




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)



    app.run(port=5000, host='0.0.0.0')