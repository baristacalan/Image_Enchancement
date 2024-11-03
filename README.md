# Image Enhancement Project
This project performs various image enhancement techniques on medical images to improve their contrast and visibility. It includes functions for gamma correction, intensity stretching, and preprocessing to aid in visualizing features more clearly. The project is implemented in Python, primarily using the SimpleITK, NumPy, and Matplotlib libraries.

# Table of Contents
###     Project Overview
###     Features
###     Installation
###     Usage
###     Directory Structure
###     Dependencies


# Project Overview
The main purpose of this project is to enhance medical images, specifically CT scans, by applying various techniques:

Gamma Correction: Adjusts contrast in images by applying a non-linear transformation.
Intensity Stretching: Expands the intensity range of the image to make features more visible.
Image Preprocessing: Converts images into a suitable format and normalizes them.
This tool is intended to help visualize hard-to-see regions in medical imaging, like bones or specific brain structures, by enhancing contrast and highlighting important features.

## Features
### Gamma Correction: Applies a gamma transformation to adjust image contrast.
### Intensity Stretching: Uses piecewise linear intensity stretching to bring out details in regions with narrow intensity ranges.
### Support for Different Image Formats: Compatible with .jpg, .png, and .tif image formats.
### Data Export: Allows saving processed images and intensity values for further analysis.
# Installation
### Clone the repository:

git clone https://github.com/baristacalan/Image_Enhancement.git
cd Image_Enhancement

### Create and activate a virtual environment (optional but recommended):

python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt
## Usage
Load an Image: Place your image files in the photos/default directory.

Run the Main Script:

python main.py

The script will:

Load the specified medical image.
Preprocess and enhance the image based on the selected method (gamma correction or intensity stretching).
Display the processed image using Matplotlib or Fiji (if installed).
Save Processed Images: Enhanced images will be saved in photos/enchanced/ directory.

Functions
loadImage(image_path: Path): Loads an image from the specified path.
preprocessImage(image: sitk.Image): Preprocesses the image by normalizing its intensity.
enhanceImage(image: sitk.Image): Applies gamma correction or intensity stretching.
showImage(image_list: list[sitk.Image], fiji_exists: bool = False): Displays images, optionally using Fiji if available.
saveImage(image: sitk.Image, save_path: Path, image_io: str = 'JPEGImageIO'): Saves the image in the specified format.
Example Code
To enhance an image and display it:

from functions import loadImage, preprocessImage, enhanceImage, showImage
from pathlib import Path

# Load and preprocess image
image_path = Path("photos/default/2.png")
image = loadImage(image_path)
image = preprocessImage(image)

# Enhance and show image
image = enhanceImage(image)
showImage([image], fiji_exists=False)

Install dependencies with:

pip install -r requirements.txt