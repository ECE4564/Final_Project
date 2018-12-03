from flask import Flask, render_template, request

app = Flask(__name__)

color = "Default"
name = "Default"
seat = "Default"

@app.route("/")
def hello():
    return render_template("main.html")

@app.route("/login")
def login():
    # Get request parameters
    global color, name, seat
    print(color + ' ' + name + ' ' + seat)

    return render_template("login.html", color=color, name=name)

@app.route("/update_info", methods=['PUT'])
def info():
    global color, name, seat

    # Get new info
    info = request.json

    # Assign new info
    color = info['Color']
    name = info['Name']
    seat = info['Seat']

    return "Success"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)