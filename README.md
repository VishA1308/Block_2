# Block_2

The program is designed to compare color histograms of two images and quantitatively assess their visual similarity based on statistical analysis of color distribution.

## get_image_path()

An interactive function for safely obtaining an image path with multi-level validation.

Operating Algorithm:

Input: Prompts the user for a file path via standard input

Empty path check: Rejects empty lines and lines containing only spaces

File existence check: Uses os.path.exists() to check the physical presence of a file

Image integrity check: Attempts to load the file using OpenCV to verify the correct format

Error handling:

Empty path: Displays a message and repeats the request

Non-existent file: Informs the user that the file does not exist

## main()

Coordinates the entire image comparison process from loading to displaying results.
Sequence of operations:

Stage 1: Processing the first image

Call get_image_path() to obtain the path

Loading a color image using load_img_color()

Checking whether the loading was successful

Scaling to a fixed size of 400x400 pixels

Plotting color histograms using plot_color_histograms()

Stage 2: Processing the second image

Similar operations for the second image

Stage 3: Comparison and analysis

Call compare_histograms() to compare histograms

Printing the average correlation coefficient

## compare_histograms(hist_1, hist_2)

Calculates the similarity measure between the histograms of two images for each color channel.
Input parameters:

hist_1 (list of numpy arrays): List of 3 histograms for the first image 

hist_2 (list of numpy arrays): Similar list for the second image

Step 1: Data Preparation

### hist1 = hist_1[i].flatten().astype(np.float32)
### hist2 = hist_2[i].flatten().astype(np.float32)

Converting multidimensional histograms to one-dimensional vectors

Cast to float32 for OpenCV compatibility

Step 2: Validation

Checking that the histograms are not zero

If the histogram is zero, set the coefficient to 0.0 and skip the channel

Step 3: Normalization

L1 normalization for casting Histograms to a single scale

The sum of all bins becomes 1

Step 4: Calculating the correlation


### similar = cv2.compareHist(hist1_norm, hist2_norm, cv2.HISTCMP_CORREL)

Using the Pearson correlation method

Range of values: -1.0 to 1.0

Returned values:

### similarity (list): List of 3 correlation coefficients

### avg_correlation (float): Arithmetic mean of all three coefficients


# Image Color Histogram

A Python application for analyzing and visualizing color distributions in images by creating histograms for Red, Green, and Blue channels. This project demonstrates fundamental computer vision concepts and image processing techniques.

## Requirements

### Python Dependencies

The following Python packages are required to run this application:

```
numpy>=1.21.0
opencv-python>=4.5.0
matplotlib>=3.5.0
```

### System Requirements

- Python 3.7 or higher
- Operating System: Windows, macOS, or Linux
- Minimum 4GB RAM (recommended for large images)

## Installation

### Method 1: Using pip (Recommended)

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd Image-color-histogram
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy opencv-python matplotlib
   ```

### Method 2: Using requirements.txt

1. Create a requirements.txt file with the following content:
   ```
   numpy>=1.21.0
   opencv-python>=4.5.0
   matplotlib>=3.5.0
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Method 3: Using conda

```bash
conda install numpy opencv matplotlib
```

## Usage

### Basic Usage

1. Run the script:
   ```bash
   python CV-1-07.py
   ```

2. Enter the path to your image when prompted:
   ```
   Enter image path: path/to/your/image.jpg
   ```

3. The application will display three histograms showing the color distribution for Red, Green, and Blue channels.

### Supported Image Formats

The application supports all image formats that OpenCV can read, including:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)

## Implementation Details

### Core Functions

- `load_img_color(img_path)`: Loads color images with error handling
- `plot_color_histograms(img)`: Creates and displays RGB channel histograms
- `main()`: Handles user input and orchestrates the workflow

## Examples

### Sample Output
<img width="300" alt="icon" src="https://github.com/user-attachments/assets/58e1c54e-9081-4c03-8399-f55b8d1745e2" />
<img width="600" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/ef15c59a-99d8-4b71-ae17-b008719f39cc" />

## Educational Context

**Novosibirsk State University (NSU)**  
**Bachelor's Program**: 15.03.06 - Mechatronics and Robotics (AI Profile)

*Project Activity Course - Task 1*  
*Computer Vision Algorithms in Python*

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## License

This project is part of an educational curriculum at Novosibirsk State University.

