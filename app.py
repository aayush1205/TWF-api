import os
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET'])
def solve():
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
