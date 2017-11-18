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

import os
from datetime import datetime
from sqlalchemy import and_
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.secret_key = "ABC"


# Raises an error in Jinja
# app.jinja_env.undefined = StrictUndefined




@app.route('/donor-info.json')
def fetch_donor_info(donor_id):

    donor = Donor.query.get(donor_id)
    donor_dict = {"id": donor.donor_id, 
                  "name": donor.name,
                  "phone": donor.phone_number,
                  "email": donor.email,
                  "address": {
                      "address": donor.address.formatted_add,
                      "lat": donor.address.lat,
                      "lng": donor.address.lng,  
                      }
                  }

    return jsonify(donor_dict)


@app.route('/receiver-info.json')
def fetch_receiver_info(receiver_id):

    receiver = Receiver.query.get(receiver_id)
    receiver_dict = {"id": receiver.receiver_id, 
                  "name": receiver.name,
                  "phone": receiver.phone_number,
                  "email": receiver.email,
                  "address": {
                      "address": receiver.address.formatted_add,
                      "lat": receiver.address.lat,
                      "lng": receiver.address.lng,  
                      }
                  }

    return jsonify(receiver_dict)


@app.route('/geocode')
def address_to_latlng(formatted_add):

    geolocator = Nominatim()
    location = geolocator.geocode(formatted_add)

    return jsonify("address": formatted_add: {"lat": location.latitude, "lng":location.longitude})


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)



    app.run(port=5000, host='0.0.0.0')