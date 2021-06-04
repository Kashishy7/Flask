from flask import Flask, request

app = Flask(__name__)

stri = ""

@app.route("/")
def hello():
    return "Hello, World!"

# @app.route("/xyz/<string:username>/<string:name>", methods=["POST", "GET"])
# def xyz(username, name):
#     return "I got a username - " + username + " name - " + name

# @app.route("/post", methods=["POST", "GET"])
# def post():
#     data = request.json
#     print(data)
#     return data

@app.route("/<s>")
def concat(s):
    global stri
    stri += " "+s
    return stri

if __name__ == "__main__":
    app.run(debug=True)
