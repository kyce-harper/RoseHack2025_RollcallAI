from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/run-python', methods=['POST'])
def run_python():
    # Run the Python script
    # result = subprocess.run(['python', 'faceRecognition.py'], capture_output=True, text=True)
    # return jsonify({
    #     "stdout": result.stdout,
    #     "stderr": result.stderr
    # })
    
    try:
        # Run the Python script in the background
        subprocess.Popen(['python', 'faceRecognition.py'])
        return jsonify({"status": "Python script started in the background"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)