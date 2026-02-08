from flask import Flask, jsonify
import psutil
import time
from flask_cors import CORS

app = Flask(__name__)

def get_system_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    return int(current_time - boot_time)

@app.route("/data")
def health_data():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    result = {
        "uptime": get_system_uptime(),   # real server uptime in seconds
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "cpu": cpu_usage,
        "memory": memory_usage
    }
    return jsonify(result)

if __name__ == "__main__":
    CORS(app)
    app.run(host="0.0.0.0", port=10001)
