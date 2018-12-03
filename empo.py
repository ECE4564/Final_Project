from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("main.html")


@app.route("/login")
def login():
    # Get request parameters
    color = request.args.get('color')
    name = request.args.get('name')
    seat = request.args.get('seat')

    return render_template("login.html", color=color, name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
