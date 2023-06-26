from src.modules.authorization import generateKey
def process(cacheManager):
    key = generateKey()
    cacheManager.add(key)
    return {
        'APIKey': key
    }