#!/usr/bin/python3
""" api for state object """

from flask import Flask, jsonify, abort
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import request

@app_views.route('/status', methods=['GET'])
def get_states():
    states = storage.all('State')
    mylist = []
    for state in states:
        mylist.append(state.to_dict())
    return jsonify(mylist)

@app_views.route('/status/<string:id>', methods=['GET'])
def state_with_id():
    state = storage.get('State', 'state_id')
    if state is None:
        abort(404)
    return jsonify(state.to_dict()), "OK"

@app_views.route('/states/', methods=['POST'])
def add_state():
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    if 'name' not in response:
        abort(400, {'Missing name'})

    stateObj =State(name=response['name'])
    storage.new(stateObj)
    storage.save()
    return jsonify(stateObj.to_dict()), '201'

@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state():
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    stateObj = storage.get('State', 'state_id')
    if stateObj is None:
        abort(404)
    removeKeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in removeKeys:
            setattr(stateObj, key)
        storage.save()

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state():
    stateObj = storage.get('State', 'state_id')
    if stateObj is None:
        abort(404)
    storage.delete(stateObj)
    storage.save()
    return jsonify({}), '200'