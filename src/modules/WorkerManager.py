from concurrent.futures import ThreadPoolExecutor
from src.configs import MAX_WORKERS
from .post_handlers import RemoveBackground
from .get_handlers import GenerateAPIKey, GenerateMask

workerManager = ThreadPoolExecutor(max_workers=MAX_WORKERS)


def handle_remove_background(datas):
    worker = workerManager.submit(RemoveBackground.process, datas)
    return worker.result()


def handle_generate_key(cacheManger):
    worker = workerManager.submit(GenerateAPIKey.process, cacheManger)
    return worker.result()


def handle_generate_mask(**kwargs):
    worker = workerManager.submit(GenerateMask.process, **kwargs)
    return worker.result()