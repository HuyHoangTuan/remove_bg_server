from PIL import Image
from rembg import remove
from flask import make_response
import io
import time

def process(datas):
    for i, data in enumerate(datas):
        file = data['file']
        image = Image.open(io.BytesIO(file.read()))
        output = remove(image)
        imageResponse = io.BytesIO()
        output.save(imageResponse, format='PNG')
        imageResponse.seek(0)

        return imageResponse

