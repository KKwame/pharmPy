from flask import Flask, jsonify, request
from training import predict

app = Flask(__name__)

@app.route("/home", methods=['POST'])
def home():
    if request.method == "POST":
        data = request.get_json(force=True)["data"]
        print(data)
        response = predict([data])
        response = response[0]
        return jsonify({"response": str(response)})


if __name__ == "__main__":
    app.run(host="192.168.43.118",port=5000)
