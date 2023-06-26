from concurrent.futures import ThreadPoolExecutor
from src.configs import MAX_WORKERS
from .post_handlers import RemoveBackground
from .get_handlers import GenerateAPIKey

workerManager = ThreadPoolExecutor(max_workers=MAX_WORKERS)

def handleRemoveBackground(datas):
    worker = workerManager.submit(RemoveBackground.process, datas)
    return worker.result()

def handleGenerateKey(cacheManger):
    worker = workerManager.submit(GenerateAPIKey.process, cacheManger)
    return worker.result()