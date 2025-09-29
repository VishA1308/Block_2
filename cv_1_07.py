import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

def load_img_color(img_path: str) -> np.ndarray:
    """
    Loads an image from the specified file path in color mode.

    Args:
        img_path (str): The path to the image file.

    Returns:
        np.ndarray: The loaded color image as a NumPy array, or None if loading fails.
    """
    img = cv.imread(img_path, cv.IMREAD_COLOR)
    if img is None:
        # Return None if the image could not be loaded (e.g., file not found or not an image)
        return None
    return img

def plot_color_histograms(img: np.ndarray) -> None:
    """
    Plots the color histograms for the red, green, and blue channels of the input image.

    Args:
        img (np.ndarray): The input color image as a NumPy array (BGR format).
    """
    # Create a figure with 3 subplots (one for each color channel)
    fig, axes = plt.subplots(1, 3, figsize=(12, 6), constrained_layout=True)
    
    channels = [
        (2, "r", "Red"),
        (1, "g", "Green"),
        (0, "b", "Blue"),
    ]
    
    histograms = []
    
    # Loop through each channel and plot its histogram
    for ax, (channel_idx, color, title) in zip(axes, channels):
        # Calculate the histogram for the current channel
        hist = cv.calcHist([img], [channel_idx], None, [256], [0, 256])
        histograms.append(hist)

        ax.hist(range(256), bins=32, weights=hist.flatten(), color=color, alpha=0.7, density=True)
        ax.set_title(f"{title} channel")
        ax.set_xlabel("Pixel value")
        ax.set_ylabel("Frequency")
    
    plt.show()

    return fig, axes, histograms
    

def main() -> None:
    """
    Main function to prompt the user for an image path, load the image,
    and display its color histograms.

    Raises:
        ValueError: If the image path is empty, the file does not exist, or the image cannot be loaded.
    """
    src = input("Enter image path: ")
    #input validation
    if not src:
        raise ValueError("Image path cannot be empty.")
    if not os.path.isfile(src):
        raise ValueError(f"File '{src}' does not exist.")

    img = load_img_color(src)

    if img is None:
        raise ValueError(f"Could not open image: {src}")
    
    plot_color_histograms(img)

if __name__ == "__main__":
    main()
