from PIL import Image, UnidentifiedImageError
from numpy import array
from load_image import ft_load

"""
This program loads an image, prints some info, then displays it.
The info are :
    - size in pixel for X and Y axis (shape)
    - the number of channels (RGB would be 3, greyscale would be 1)
    - the pixel content
"""


def convert_to_greyscale(image_array):
    # Convert the image array to a PIL Image
    img = Image.fromarray(image_array)
    # Convert the image to greyscale
    grey_img = img.convert('L')
    # Convert the greyscale image back to a numpy array
    grey_array = array(grey_img)
    return grey_array


# def zoom_img(img_array, new_width, new_height):
#     img = Image.fromarray(img_array)
#     zoomed_img = img.resize(new_width, new_height)
#     zoomed_array = array(zoomed_img)
#     return zoomed_array

from PIL import Image

def zoom_img(img, new_width, new_height):
    zoomed_img = img.resize((new_width, new_height))
    return zoomed_img

def main():
    """
    Check the input is valid.
    Prints the input converted to MORSE code.
    """
    anim_array = ft_load("animal.jpeg")
    if anim_array is not None:
        print(anim_array)
        new_width = 400
        new_height = 400
        zoomed_array = zoom_img(anim_array, new_width, new_height)
        final_img = Image.fromarray(zoomed_array)
        final_img.show()
        # grey_array = convert_to_greyscale(zoomed_array)
        # # print("greay shaope -", grey_array.shape) ##

        # final_img = Image.fromarray(grey_array)
        # final_img.show()

if __name__ == "__main__":
    main()