from flask import Flask, request, jsonify
import json
import AuthDB

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
        print(str(content))
        res = db.change_status({'Tag': content['Tag']}, content['Status'])
        print(res)
        print(res['Name'])
        return jsonify(res)
    except:
        return 'Error in change_user_status()'


if __name__ == '__main__':
    db = AuthDB.AuthDB()
    app.run(host='0.0.0.0')
