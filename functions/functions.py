import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from pathlib import Path
def getPixelValues(image :sitk.Image) -> pd.DataFrame:

    r"""
    Takes the image as input and creates a dataframe for each (x,y) intensity values.

    :param image:
    :return: pd.DataFrame

    :returns: a pandas Dataframe containing intensity values and a list
    """

    WIDTH = image.GetWidth()
    HEIGHT = image.GetHeight()
    pixel_values=[]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            pixel = image.GetPixel(x, y)
            pixel_values.append({"x" : x, "y" : y, "intensity" : pixel})
    pixel_df = pd.DataFrame(pixel_values)
    return pixel_df
def loadImage(imagepath :Path) -> sitk.Image:
    """
    :param imagepath: Path of the Image as a string.
    :return: A sitk.Image object as image.
    """
    image = sitk.ReadImage(fileName=imagepath)
    return image
def saveImage(image: sitk.Image, save_path: Path, image_io :str = 'JPEGImageIO') -> None:
    image = sitk.RescaleIntensity(image, 0, 255)
    image = sitk.Cast(image, sitk.sitkUInt8)

    writer = sitk.ImageFileWriter()
    writer.SetImageIO(image_io)  # Set the format; adjust if necessary
    writer.SetFileName(save_path)
    writer.Execute(image)  # Directly save the image without assignment
def toArray(image :sitk.Image) -> np.array:
    img_array =sitk.GetArrayFromImage(image)
    return img_array
def preprocessImage(image :sitk.Image) -> sitk.Image:
    if image.GetPixelIDValue() == 13:
        image = sitk.VectorMagnitude(image)

    #image_array = sitk.GetArrayFromImage(image).astype('float32') / 255.0
    immage_array = toArray(image)
    image_array = immage_array.astype('float32') / 255.0
    image = sitk.GetImageFromArray(image_array)
    return image
def showImages(image_list :list[sitk.Image], fiji_exists: bool = False) -> None:

    """
    Displays the images in either Fiji or using Matplotlib API.

    :param image_list: List of sitk.Image
    :param fiji_exists: Default=False. If Fiji exists in your computer, you may set to True.
    :return: None
    """

    if fiji_exists:

        for i, image in enumerate(image_list):
            sitk.Show(image, title=f"Image {i + 1}")

    else:
        # Determine the number of images and display them side-by-side
        image_num = len(image_list)
        plt.figure(figsize=(20, 10))

        for i in range(image_num):
            plt.subplot(1, image_num, i + 1)
            if i == 0:
                plt.title("Before")
            else:
                plt.title("After")
            #plt.title(f'Photo {i + 1}')
            plt.imshow(sitk.GetArrayFromImage(image_list[i]), cmap='gray')
            plt.axis('off')

        plt.show()  # Show all images in one figure
def transformIntensity(intensity :float, gama :float) -> int:
    A = 1.4
    new_intensity = A * math.pow(intensity, gama) * 255
    return min(max(int(new_intensity), 0), 255)
def stretchImage(image :sitk.Image) -> sitk.Image:
    image = sitk.RescaleIntensity(image, outputMinimum=0, outputMaximum=255)
    return image
def enchanceImage(image :sitk.Image) -> sitk.Image:
    WIDTH, HEIGHT = image.GetWidth(), image.GetHeight()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            curr_intensity = image.GetPixel(x, y)
            if round(curr_intensity) == 0:
                new_intensity = transformIntensity(curr_intensity, gama=0.3)
            else:
                new_intensity = transformIntensity(curr_intensity, gama=1.8)

            image.SetPixel(x, y, new_intensity)
    return image