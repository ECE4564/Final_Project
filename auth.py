from flask import Flask, request, jsonify
import json
import AuthDB
import logging
import socket
import sys
import signal

app = Flask(__name__)


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
