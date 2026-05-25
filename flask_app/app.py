from flask import Flask, jsonify
# Import thư viện exporter
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

#  Khởi tạo PrometheusMetrics và gắn nó vào app Flask
# Tham số path='/metrics' sẽ tự động tạo ra một đường dẫn http://localhost:5000/metrics
metrics = PrometheusMetrics(app, path='/metrics')

# 3. Thêm một số thông tin tĩnh (Static Info) để hiển thị trên Dashboard cho đẹp
metrics.info('app_info', 'Flask Application info', version='1.0.0')

@app.route("/")
def home():
    return jsonify({"message": "Hello from Demo App!", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

# @app.route("/health01")
# def health01():
    # return jsonify({"status": "healthy 08"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
