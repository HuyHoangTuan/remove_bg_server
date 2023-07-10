import numpy as np
from scipy.ndimage import grey_erosion, grey_dilation, median_filter
from PIL import Image


def generate_mask_for_removed_background_image(removed_background_image):
    # removed_background_image = median_filter(removed_background_image, size=3)
    image_np = np.array(removed_background_image)

    alpha_threshold = np.median(np.unique(image_np[:, :, 3]))

    mask_np = np.zeros(image_np.shape, dtype=np.uint8)
    mask_np[:, :, 3] = image_np[:, :, 3]
    alpha_np = mask_np[:, :, 3]

    # for row in range(0, alpha_np.shape[0]):
        # for col in range(0, alpha_np.shape[1]):
            # if alpha_np[row, col] >= alpha_threshold:
                # alpha_np[row, col] = 1

    structure_np = np.array(
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
    )

    eroded_alpha_np = grey_erosion(alpha_np, structure=structure_np).astype(alpha_np.dtype)
    dilated_alpha_np = grey_dilation(eroded_alpha_np, structure=structure_np).astype(alpha_np.dtype)

    binary_mask_np = dilated_alpha_np

    mask_np = image_np
    for row in range(0, mask_np.shape[0]):
        for col in range(0, mask_np.shape[1]):
            if binary_mask_np[row, col] < alpha_threshold:
                mask_np[row, col, 3] = 0
            else:
                mask_np[row, col, 0] = 98
                mask_np[row, col, 1] = 236
                mask_np[row, col, 2] = 241
                mask_np[row, col, 3] = 255
        
    return Image.fromarray(mask_np)
