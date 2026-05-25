from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Demo App!", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/health01")
def health01():
    return jsonify({"status": "healthy 08"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
