import time
import subprocess
from flask import Flask, jsonify, request
from celery import Celery
import redis
from flask_cors import CORS
from modules import urls

app = Flask(__name__)
CORS(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker='redis://localhost:6379/0',
        backend='redis://localhost:6379/0'
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

@celery.task(bind=True)
def processes(self, url):
    run_nmap(url)

    if self.is_aborted:
        return "Aborted"

@app.route('/scan/abort/<task_id>', methods=['GET'])
def abort_scan(task_id):
    print(task_id)
    redis_client.set(f"scan:{task_id}", "ABORTED")
    return jsonify({"status": "aborted"}), 200

@celery.task
def run_nmap(url):
    print("Hrer")
    time.sleep(2) 
    return {"url": url, "message": "completed", "ports": [22, 80, 443]}

# def run_nmap(url):
#     try:
#         result = subprocess.run(["nmap", "-T4", "-F", url ], capture_output=True, text=True, check=True)

#         return jsonify({"data": result.stdout})
        
#     except subprocess.CalledProcessError as e:
#         return jsonify({"message": str(e)}), 500
    
@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"message": "URL is required"}), 400

    if not urls.check_url_validity(url):
        return jsonify({"message": "Invalid URL or cannot be reached"}), 400

    task = run_nmap.apply_async(args=[url]) 

    return jsonify({
        "message": "Your scan is running",
        "task_id": task.id
    }), 202

# @app.route('/scan_status/<task_id>', methods=['GET'])
# def scan_status(task_id):
#     task = run_scan.AsyncResult(task_id)
#     if task.state == 'PENDING':
#         response = {'state': task.state, 'progress': 0}
#     elif task.state == 'PROGRESS':
#         response = {'state': task.state, 'progress': task.info.get('progress', 0)}
#     elif task.state == 'SUCCESS':
#         response = {'state': task.state, 'result': task.result}
#     else:
#         response = {'state': task.state}
#     return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
