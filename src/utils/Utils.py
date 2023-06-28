import numpy as np
from scipy.ndimage import binary_erosion, binary_dilation
from PIL import Image
def generate_mask_for_removed_background_image(removed_background_image):
    image_np = np.array(removed_background_image)

    alpha_threshold = np.median(image_np[:, :, 3])
    mask_np = np.zeros(image_np.shape, dtype=np.uint8)
    mask_np[:, :, 3] = image_np[:, :, 3]
    alpha_np = mask_np[:, :, 3]
    
    for row in range(0, alpha_np.shape[0]):
        for col in range(0, alpha_np.shape[1]):
            if alpha_np[row, col] >= alpha_threshold:
                alpha_np[row, col] = 1

    structure_np = np.array([[0, 1, 0],
                     [1, 1, 1],
                     [0, 1, 0]])
    
    eroded_alpha_np = binary_erosion(alpha_np, structure=structure_np).astype(alpha_np.dtype)
    dilated_alpha_np = binary_dilation(eroded_alpha_np, structure=structure_np).astype(eroded_alpha_np.dtype)
    
    mask_np = image_np
    for row in range(0, mask_np.shape[0]):
        for col in range(0, mask_np.shape[1]):
            if dilated_alpha_np[row, col] == 0:
                mask_np[row, col, 3] = 0

    return Image.fromarray(mask_np)