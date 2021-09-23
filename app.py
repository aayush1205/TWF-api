import os
from flask import Flask, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def solve():
    if request.method == 'GET':
        return "<h1>Welcome!</h1>"
    else:

        req = request.get_json()
        try:
            inp = req["input"]
        except:
            abort(400)
        with open("input.txt", "w+") as f:
            f.write(inp)
        stream = os.popen('./a.out < input.txt')
        output = stream.read()
        return output, 200


if __name__ == "__main__":
    app.run(debug=True)
