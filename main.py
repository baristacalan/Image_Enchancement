from functions import loadImage, preprocessImage, stretchImage, saveImage, showImages, enchanceImage
import SimpleITK as sitk
from pathlib import Path
def main():

    #First Image
    Path("photos/enchanced").mkdir(parents=True, exist_ok=True)

    image_1 = loadImage('photos/default/1.jpg')

    image_default_1 = sitk.Image(image_1)

    image_1 = preprocessImage(image_1)

    image_enchanced_1 = enchanceImage(image_1)

    showImages([image_default_1, image_enchanced_1], False)

    #SECOND IMAGE

    image_2 = loadImage('photos/default/2.png')

    image_default_2 = sitk.Image(image_2)

    image_2 = preprocessImage(image_2)

    image_enchanced_2 = stretchImage(image_2)

    saveImage(image_enchanced_2, 'photos/enchanced/2.png', image_io='PNGImageIO')

    showImages([image_default_2, image_enchanced_2], False)

    return 0

if __name__ == '__main__':
    main()