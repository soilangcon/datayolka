#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

"""
def to_grayscale(image_path="src/painting.png"):
    image = plt.imread(image_path)
    image = image.copy()
    gray_image = image[:,:, 0]*0.2126 + image[:, :, 1]*0.7152+ image[:, :, 2]*0.0722
    return gray_image
"""
def to_grayscale(image):
    return np.dot(image[...,:3], np.array([0.2126, 0.7152, 0.0722]))

def to_red(imarr):
    imarr = imarr.copy()
    imarr[:, :, 1], imarr[:, :, 2] = 0.0, 0.0
    return imarr

def to_green(imarr):
    imarr = imarr.copy()
    imarr[:, :, 0], imarr[:, :, 2] = 0.0, 0.0
    return imarr

def to_blue(imarr):
    imarr = imarr.copy()
    imarr[:, :, 0], imarr[:, :, 1] = 0.0, 0.0
    return imarr

def main():
    # Read the image using Matplotlib
    image_path = 'src/painting.png'  # Replace with your image path
    image = plt.imread(image_path)
    gray_image = to_grayscale(image)
    plt.gray()
    plt.imshow(gray_image)
    plt.show()

    
    red_image = to_red(image)
    green_image = to_green(image)
    blue_image = to_blue(image)
    
    fig, axs = plt.subplots(3, 1, figsize=(5, 15))
    
    axs[0].imshow(red_image)
    axs[0].set_title('Red Image')
    axs[0].axis('off')
    
    axs[1].imshow(green_image)
    axs[1].set_title('Green Image')
    axs[1].axis('off')
    
    axs[2].imshow(blue_image)
    axs[2].set_title('Blue Image')
    axs[2].axis('off') 
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
