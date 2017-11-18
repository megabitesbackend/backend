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
from datetime import datetime, timedelta
from sqlalchemy import and_
from geopy.geocoders import Nominatim


app = Flask(__name__)
app.secret_key = "ABC"


# Raises an error in Jinja
# app.jinja_env.undefined = StrictUndefined

@app.route('/donor-info.json')
def fetch_donor_info(donor_id):

    # donor = Donor.query.get(donor_id)
    donor_dict = {"id": 1, 
                  "name": "Chez Panisse",
                  "phone": "(510) 548-5525",
                  "email": "alice@chezpanisse.com",
                  "address": {
                      "address": "1517 Shattuck Ave, Berkeley, CA 94709",
                      "lat": 37.8796128,
                      "lng": -122.2710068,  
                      }
                  }

    return jsonify(donor_dict)


@app.route('/receiver-info.json')
def fetch_receiver_info(receiver_id):

    receiver = Receiver.query.get(receiver_id)
    receiver_dict = {"id": 1, 
                  "name": "SF-Marin Food Bank",
                  "phone": "(415)282-1900",
                  "email": "paul@sf-marinfoodbank.org",
                  "address": {
                      "address": "900 Pennsylvania Ave., SF, CA 94107",
                      "lat": 37.7544355,
                      "lng": -122.395706,  
                      }
                  }

    return jsonify(receiver_dict)


@app.route('/pickups', methods=['GET', 'POST'])
def fetch_pickup_info():
    """Dictionary of food items that have not been claimed"""
    available_pickups = {1: {{"name": "Chez Panisse",
                                 "phone": "(510) 548-5525",
                                 "email": "alice@chezpanisse.com",
                                 "address": {
                                    "address": "1517 Shattuck Ave, Berkeley, CA 94709",
                                    "lat": 37.8796128,
                                    "lng": -122.2710068
                                  }
                                }, 
                                "foodItems": [
                                    {"id": 1,
                                    "name": "Fort Bragg rockfish",
                                    "servings": 20,
                                    "expiration_date": datetime.now() + timedelta(days=2)
                                    },                            
                                    {"id": 2,
                                    "name": "Chantrelle mushrooms",
                                    "servings": 40,
                                    "expiration_date": datetime.now() + timedelta(days=15)
                                    }, 
                                    {"id": 3,
                                    "name": "Leeks",
                                    "servings": 35,
                                    "expiration_date": datetime.now() + timedelta(days=10)
                                    }
                                ]},
                                2: {{"name": "Jupiter Taproom",
                                   "phone": "(510)843-8277",
                                   "email": "bob@jupitertaproom.com",
                                   "address": {
                                      "address": "2181 Shattuck Ave, Berkeley, CA 94704",
                                      "lat": 37.8697972,
                                      "lng": -122.2697709  
                                    }
                                  }, 
                                "foodItems": [
                                    {"id": 1,
                                    "name": "Fort Bragg rockfish",
                                    "servings": 20,
                                    "expiration_date": datetime.now() + timedelta(days=2)
                                    },                            
                                    {"id": 2,
                                    "name": "Chantrelle mushrooms",
                                    "servings": 40,
                                    "expiration_date": datetime.now() + timedelta(days=15)
                                    }, 
                                    {"id": 3,
                                    "name": "Leeks",
                                    "servings": 35,
                                    "expiration_date": datetime.now() + timedelta(days=10)
                                    }]}, 
                                3: {{"name": "Whitechapel",
                                   "phone": "(415)292-5800",
                                   "email": "unicorn@whitechapel.com",
                                   "address": {
                                      "address": "600 Polk St., SF, CA 94102",
                                      "lat": 37.7823999,
                                      "lng": -122.4210646  
                                    }}, 
                                    "foodItems": [
                                        {"id": 1,
                                        "name": "Hamburgers",
                                        "servings": 20,
                                        "expiration_date": datetime.now() + timedelta(days=2)
                                        },                            
                                        {"id": 2,
                                        "name": "Chantrelle mushrooms",
                                        "servings": 40,
                                        "expiration_date": datetime.now() + timedelta(days=15)
                                        }, 
                                        {"id": 3,
                                        "name": "Leeks",
                                        "servings": 35,
                                        "expiration_date": datetime.now() + timedelta(days=10)
                                        }                                
                                    ]}}

    if request.method = "GET":
        # food_lst = Food.query.filter(receiver_id = None).all()
        
        return jsonify(available_pickups) 

    elif request.method = "POST":  

        available_pickups = available_pickups[1]["foodItems"] = {"id": 4,
                                                                 "name": "Carrots",
                                                                 "servings": 20,
                                                                 "expiration_date": datetime.now() + timedelta(days=10)
                                    }

        return jsonify(available_pickups) 


@app.route('/claims')
def fetch_claim_info():
    """Dictionary of food items that have not been claimed"""

    # food_lst = Food.query.filter(receiver_id = None).all()
    claimed_items = {1: {{"name": "Chez Panisse",
                         "phone": "(510) 548-5525",
                         "email": "alice@chezpanisse.com",
                         "address": {
                            "address": "1517 Shattuck Ave, Berkeley, CA 94709",
                            "lat": 37.8796128,
                            "lng": -122.2710068,  
                          }}, 
                        "foodItems": [
                        {"id": 4,
                        "name": "Duck breast",
                        "servings": 12,
                        "expiration_date": datetime.now() + timedelta(days=5)
                        },
                        {"id": 5,
                        "name": "Hazelnut ice cream",
                        "servings": 23,
                        "expiration_date": datetime.now() + timedelta(days=30)
                        }                               
                            ]}
    }   

    return jsonify(claimed_items) 


##HELPER FUNCTION

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