from flask import Flask, request, jsonify
import json
import AuthDB
import logging
import socket
import sys
import signal

app = Flask(__name__)


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        content = request.json
        res = db.insert(content)
        return res
    except:
        return 'Error in add()'


@app.route('/change_status', methods=['PUT'])
def change_user_status():
    try:
        content = request.json
        res = db.change_status(content['Tag'], content['Status'])
        return res
    except:
        return 'Error in change_user_status()'


if __name__ == '__main__':
    db = AuthDB.AuthDB()
    app.run(host='0.0.0.0')
