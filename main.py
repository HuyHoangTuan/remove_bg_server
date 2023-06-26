from flask import Flask, request, make_response, abort
from flask_cors import CORS
from src.configs import CONFIG
from src.modules import WorkerManager
from src.modules.authorization import generateKey
from src.modules.cache import CacheManager

app = Flask(__name__)
CORS(app, origins= CONFIG['accepted_origin'])
cacheManger = CacheManager()
cacheManger.reset()

def validateApiKey(rq):
    args = rq.args
    api_key = args.get('key')
    if api_key is None:
        return abort(403, 'Invalid API Key')
    if cacheManger.isExist(api_key) is False:
        return abort(403, 'Invalid API Key')
    return True

@app.route('/api/test_api', methods = ['GET'])
def test_api():
    return {
        'status': 'success'
    }

@app.route('/api/generate_key', methods = ['GET'])
def processGenerateKey():
    return WorkerManager.handleGenerateKey(cacheManger)

@app.route('/api/remove_background', methods = ['POST'])
def processRemoveBackground():
    validateResult = validateApiKey(request)
    if validateResult is not True:
        return validateResult
    
    files = []
    for fileName in request.files:
        files.append(
            {
                'fileName': fileName,
                'file': request.files[fileName]
            }
        )
    
    if len(files) < 1:
        return abort(415, 'Unsupported Media Type')
    
    data = WorkerManager.handleRemoveBackground(files)
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Disposition'] = 'inline; filename=result.png'
    return response
 
if __name__ == '__main__':
    default_key = '6358a1fa5924e93498833626da90e7d5'
    cacheManger.add(default_key)
    print(f'Default API KEY: {default_key}')
    app.run(host = CONFIG['address'], port = CONFIG['port'], debug=True)