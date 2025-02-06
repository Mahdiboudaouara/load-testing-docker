from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Load Testing App!"

@app.route('/heavy')
def heavy_task():
    time.sleep(2)  # Simulating a heavy request
    return "Processed a heavy request!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
