from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(array: np.array, zoom_factor: float, new_w: int,
            new_h: int, channels) -> np.array:
    """
    Zoom into the array to create a window of specified size
    Print the new shape and array
    Args:
        array (numpy array): The array to resize into.
        zoom_factor (int): The factor by which to zoom in.
        new_width (int): The width of the new array.
        new_height (int): The height of the new array.
        channels (int): The number of channels in the array.
    Returns:
        np.array: The resized array
    """
    if not isinstance(array, np.ndarray):
        raise TypeError("This is not an array")
    if not isinstance(zoom_factor, float) or zoom_factor <= 0:
        raise ValueError("The zoom factor must be a positive float")
    if not isinstance(new_w, int) or new_w < 0:
        raise ValueError("The new width must be an int greater than 0")
    if not isinstance(new_h, int) or new_h < 0:
        raise ValueError("The new height must be an int greater than 0")
    if not isinstance(channels, int) or channels < 0:
        raise ValueError("The number of channels must be an int\
                         greater than 0")
    array = array[:new_h, :new_w, :channels]
    print(f"New shape after slicing: {array.shape} or ({new_h}, {new_w})")
    print(array)
    return array


def main():
    """
    Load an image, prints its info, modify the image, displays it.
    The info are :
        - size in pixel for X and Y axis (shape)
        - the number of channels (RGB would be 3, greyscale would be 1)
        - the pixel content
    The alterations are :
        - convert to grayscale
        - add a zoom factor
        - resize
        - add a border and a scale
    """
    animal_array = ft_load("animal.jpeg")
    if animal_array is not None:
        print(animal_array)
        zoom_factor = 2.25
        new_width = 400
        new_height = 400
        channels = 1
        try:
            # zoom and crop array, then print it and its shape
            animal_array = ft_zoom(animal_array, zoom_factor, new_width,
                                   new_height, channels)

            # display the image with matplotlib
            plt.imshow(animal_array, cmap='gray' if channels == 1 else None)
            plt.show()
        except Exception as e:
            print(f"An error occurred: {e}")
            return


if __name__ == "__main__":
    main()
