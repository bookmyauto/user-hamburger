import  logging
import  requests
import  threading
import  json
from    flask   import Flask
from    flask   import request
from    hamburger   import Hamburger
from    urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


logging.basicConfig(level=logging.INFO)
app             = Flask(__name__)

default_error   = json.dumps({"error_code": 500, "error_message": "Internal server error", "display_message": ""})

print("user-hamburger started")
@app.route("/v1")
def working():
    return "user-hamburger service running"

@app.route("/v1/getName", methods=["GET"])
def getName():
    try:
        if request.method == "GET":
            user_number     = request.args["userNumber"]
            response        = json.dumps(Hamburger.get_name(user_number))
            return response
    except RuntimeError as e:
        logging.critical("failure in v1/getName with error: " + str(e))
        return default_error

@app.route("/v1/setName", methods=["POST"])
def setName():
    try:
        if request.method == "POST":
            user_number     = request.args["userNumber"]
            name            = request.form["name"]
            response        = json.dumps(Hamburger.set_name(user_number, name))
            return response
    except RuntimeError as e:
        logging.critical("failure in v1/setName with error: " + str(e))
        return default_error

@app.route("/v1/history", methods=["GET"])
def history():
    try:
        if request.method == "GET":
            user_number     = request.args["userNumber"]
            count           = request.args["count"]
            last_timestamp  = requets.args["lastTimestamp"]
            response        = json.dumps(Hamburger.history(user_number, count, last_timestamp))
            return response
    except RuntimeError as e:
        logging.critical("failure in v1/history with error: " + str(e))
        return default_error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7006, debug=True, ssl_context='adhoc')
