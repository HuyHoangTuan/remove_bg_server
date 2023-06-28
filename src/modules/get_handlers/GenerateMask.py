from PIL import Image
from rembg import remove
import io
import numpy as np
from src.utils import Utils

def process(**kwargs):
    file_name = kwargs['file_name']
    file = kwargs['file']
    image = Image.open(io.BytesIO(file.read()))
    removed_background_image = remove(image)
    
    mask = Utils.generate_mask_for_removed_background_image(removed_background_image)
    response = io.BytesIO()
    mask.save(response, format='PNG')
    response.seek(0)
    return response
