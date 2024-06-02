#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    try: height, width, _ = a.shape
    except: height, width = a.shape 
    # return height/2, width/2  # note the order: (center_y, center_x)
    return (height - 1) / 2, (width - 1) / 2

def radial_distance(a):
    center_y, center_x = center(a)
    try: height, width, _ = a.shape 
    except: height, width = a.shape
    y_indices, x_indices = np.indices((height, width))
    """
    array([[[0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4]],

        [[0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4]]])
    """
    return np.sqrt((x_indices - center_x)**2 + (y_indices - center_y)**2)

def scale(a, tmin=0.0, tmax=1.0):
    """
    Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    return np.full(a.shape, a.max()) if a.min() == a.max() else tmin + (a - a.min()) * (tmax - tmin) / (a.max() - a.min())

def radial_mask(a):
    distances = radial_distance(a)
    scaled_distances = scale(distances, tmin=0.0, tmax=1.0)
    mask = 1.0 - scaled_distances
    center_y, center_x = center(a)
    mask[int(round(center_y)), int(round(center_x))] = 1.0
    return mask 

def radial_fade(a):
    if a.ndim == 3: return a*radial_mask(a)[:, :, np.newaxis]
    else: return a*radial_mask(a)  


def main():
    image = plt.imread('src/painting.png')
    
    mask = radial_mask(image)
    
    faded_image = radial_fade(image)
    
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))
    
    # Display the original image
    axs[0].imshow(image)
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    
    # Display the radial mask
    axs[1].imshow(mask, cmap='gray')
    axs[1].set_title('Radial Mask')
    axs[1].axis('off')
    
    # Display the faded image
    axs[2].imshow(faded_image)
    axs[2].set_title('Faded Image')
    axs[2].axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
