from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online"})

@app.route("/webhook", methods=["POST"])
def webhook():
    print("\n===== WEBHOOK RECEIVED =====")
    print("IP:", request.remote_addr)
    print("Headers:", dict(request.headers))
    print("Body:", request.get_data(as_text=True))
    print("============================\n")

    return jsonify({
        "success": True,
        "received": True
    }), 200
