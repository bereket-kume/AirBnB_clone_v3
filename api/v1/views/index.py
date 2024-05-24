#!/usr/bin/python3
""" api content """
from models import storage
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """ return status"""
    return jsonify({"status":"OK"})
