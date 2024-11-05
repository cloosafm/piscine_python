from PIL import Image
from numpy import dot, ndarray


def ft_invert(land_array: ndarray) -> ndarray:
    """
    Inverts the color of the image received.
    """
    land_invert = land_array.copy()
    land_invert = 255 - land_invert
    landscape_img = Image.fromarray(land_invert)
    landscape_img.show()
    return land_invert


def ft_red(land_array: ndarray) -> ndarray:
    """
    Converts the received image to red.
    """
    land_red = land_array.copy()
    land_red[:, :, 1] = 0  # Green channel set to 0
    land_red[:, :, 2] = 0  # Blue channel set to 0
    landscape_img = Image.fromarray(land_red)
    landscape_img.show()
    return land_red


def ft_green(land_array: ndarray) -> ndarray:
    """
    Converts the received image to green.
    """
    land_green = land_array.copy()
    land_green[:, :, 0] = 0  # Red channel set to 0
    land_green[:, :, 2] = 0  # Blue channel set to 0
    landscape_img = Image.fromarray(land_green)
    landscape_img.show()
    return land_green


def ft_blue(land_array: ndarray) -> ndarray:
    """
    Converts the received image to blue.
    """
    land_blue = land_array.copy()
    land_blue[:, :, 0] = 0  # Red channel set to 0
    land_blue[:, :, 1] = 0  # Green channel set to 0
    landscape_img = Image.fromarray(land_blue)
    landscape_img.show()
    return land_blue


def ft_grey(land_array: ndarray) -> ndarray:
    """
    Converts the received image to greyscale.
    Uses the luma weighted formula :
    Y'=0.299R'+0.587G'+0.114B'
    https://e2eml.school/convert_rgb_to_grayscale.html
    """
    land_grey = dot(land_array[..., :3], [0.299, 0.587, 0.114])
    # the three dots mean "all preceding dimensions", to select all pixels
    # then dot/scalar product of rgb array by the weighted values
    landscape_img = Image.fromarray(land_grey)
    landscape_img.show()
    return land_grey
