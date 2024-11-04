from PIL import Image, UnidentifiedImageError
from numpy import array


def ft_load(path: str) -> array:
    """Load an image.
     Print its format (height, width, number of channels).
     Then its pixels content in RGB format.
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"FileNotFoundError: The file at path '{path}' does not exist.")
        return None
    except UnidentifiedImageError:
        print(f"UnidentifiedImageError: \
              The file at path '{path}' is not a valid image.")
        return None
    else:
        img_array = array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array
