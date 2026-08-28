from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "Webhook API is running"
    })


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)

    return jsonify({
        "success": True,
        "received": data
    }), 200
