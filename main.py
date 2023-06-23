from flask import Flask, request
from src.configs import CONFIG
from src.modules import WorkerManager

app = Flask(__name__)

@app.route('/api/test_api', methods = ['GET'])
def test_api():
    return {
        'status': 'success'
    }

@app.route('/api/remove_background', methods = ['POST'])
def processRemoveBackground():
    return WorkerManager.handleRemoveBackground(request.data)

if __name__ == '__main__':
    app.run(host = CONFIG['address'], port = CONFIG['port'], debug=True)