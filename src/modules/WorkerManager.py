from concurrent.futures import ThreadPoolExecutor
from src.configs import MAX_WORKERS
from .post_handlers import RemoveBackground
workerManager = ThreadPoolExecutor(max_workers=MAX_WORKERS)

def handleRemoveBackground(body):
    worker = workerManager.submit(RemoveBackground.process, body)
    return worker.result()