from __future__ import print_function

import json
import os
from compiler import compiler

from flask import Flask, make_response, request
from future.standard_library import install_aliases

install_aliases()

# Flask app should start in global layout
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Network Intent Assistent (Nia) Deploy APIs"


@app.route("/deploy", methods=["POST"])
def deploy():
    req = request.get_json(silent=True, force=True)

    print("Request: {}".format(json.dumps(req, indent=4)))
    try:
        res = compiler.handle_request(req)
    except Exception as err:
        print(err)
        res = {"status": {'code': 404, 'details': 'Could not deploy intent.'}}
    res = json.dumps(res, indent=4)
    print("Response: {}".format(json.dumps(res, indent=4)))

    r = make_response(res)
    r.headers["Content-Type"] = "application/json"
    return r


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host="0.0.0.0")
