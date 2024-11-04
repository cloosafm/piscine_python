from PIL import Image, ImageOps, ImageDraw, ImageFont
from numpy import array, expand_dims, dot, uint8


# def ft_invert(land_array: array) -> array:
#     """
#     Inverts the color of the image received.
#     """
#     landscape_img = Image.fromarray(land_array)
#     landscape_img = ImageOps.invert(landscape_img)
#     landscape_img.show()
#     return array(landscape_img)


def ft_invert(land_array: array) -> array:
    """
    Inverts the color of the image received.
    """
    land_array = 255 - land_array
    landscape_img = Image.fromarray(land_array)
    landscape_img.show()
    return land_array


#     land_array[:, :, 0]  # red channel
#     land_array[:, :, 1]  # green channel
#     land_array[:, :, 2]  # blue channel

def ft_red(land_array: array) -> array:
    """
    Converts the received image to red.
    """
    land_array[:, :, 1] = 0  # green channel
    land_array[:, :, 2] = 0  # blue channel
    landscape_img = Image.fromarray(land_array)
    landscape_img.show()
    return land_array



def ft_green(land_array: array) -> array:
    """
    Converts the received image to green.
    """
    land_array[:, :, 0] = 0  # red channel
    land_array[:, :, 2] = 0  # blue channel
    landscape_img = Image.fromarray(land_array)
    landscape_img.show()
    return land_array


def ft_blue(land_array: array) -> array:
    """
    Converts the received image to blue.
    """
    land_array[:, :, 0] = 0  # red channel
    land_array[:, :, 1] = 0  # green channel
    landscape_img = Image.fromarray(land_array)
    landscape_img.show()
    return array(landscape_img)


def ft_grey(land_array: array) -> array:
    """
    Converts the received image to greyscale.
    """
    grey_array = dot(land_array[..., :3], [0.299, 0.587, 0.114]).astype(uint8)
    landscape_img = Image.fromarray(grey_array)
    landscape_img.show()
    return grey_array
