from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/nobelprize")
def get_universities():
    category = request.args.get("category")
    year = request.args.get("year")
    r = requests.get(f"https://api.nobelprize.org/2.1/nobelPrize/{category}/{year}")
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)