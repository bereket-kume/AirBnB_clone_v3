#!/usr/bin/python3
""" api content """
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """ return status"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def data():
    """ return number of data in the form dict"""
    data_num = {
        'state': State,
        'user': User,
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review
    }

    for data in data_num:
        data_num[data] = storage.count(data_num[data])
    return jsonify(data_num)
