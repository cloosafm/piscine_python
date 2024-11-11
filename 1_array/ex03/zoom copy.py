from PIL import Image, ImageOps, ImageDraw, ImageFont
from load_image import ft_load
from numpy import array


def draw_scale(image: Image.Image, border_width: int,
               scale_interval: int = 50) -> Image.Image:
    """
    Draw a scale on the image to show dimensions.
    Args:
        image (PIL.Image): The image on which to draw the scale.
        border_width (int): The width of the border around the image.
        scale_interval (int): The interval between scale marks in pixels.
    Returns:
        PIL.Image: The image with the scale and a black border line.
    """
    if not isinstance(image, Image.Image):
        raise TypeError("The image is not a PIL Image")
    if not isinstance(border_width, int) or border_width <= 0:
        raise ValueError("The border width must be an int greater than 0")
    if not isinstance(scale_interval, int) or scale_interval <= 0:
        raise ValueError("The scale interval must be an int greater than 0")

    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.load_default()

    # Draw horizontal scale
    for x in range(border_width, width - scale_interval, scale_interval):
        draw.line((x, height - border_width, x, height - border_width + 10),
                  fill="black")
        draw.text((x, height - border_width + 20), str(x - border_width),
                  fill="black", font=font)

    # Draw vertical scale
    for y in range(border_width, height - scale_interval, scale_interval):
        draw.line((border_width, y, border_width - 10, y), fill="black")
        draw.text((border_width - 30, y), str(y - border_width), fill="black",
                  font=font)

        draw.rectangle([(border_width, border_width),
                        (width - border_width, height - border_width)],
                       outline="black", width=1)

    return image


def ft_zoom(image: Image.Image, zoom_factor: float, new_width: int,
            new_height: int) -> Image.Image:
    """
    Zooms into the image and create a window of specified size
    Args:
        image (PIL.Image): The image to zoom into.
        zoom_factor (int): The factor by which to zoom in.
        new_width (int): The width of the new window.
        new_height (int): The height of the new window.
    Returns:
        PIL.Image: The zoomed-in image
    """
    if not isinstance(image, Image.Image):
        raise TypeError("The image is not a PIL Image")
    if not isinstance(zoom_factor, float) or zoom_factor <= 0:
        raise ValueError("The zoom factor must be a positive float")
    if not isinstance(new_width, int) or new_width < 0:
        raise ValueError("The new width must be an int greater than 0")
    if not isinstance(new_height, int) or new_height < 0:
        raise ValueError("The new height must be an int greater than 0")

    width, height = image.size
    new_size = (int(width * zoom_factor), int(height * zoom_factor))
    image = image.resize(new_size, Image.Resampling.BICUBIC)
    center_x, center_y = new_size[0] // 2, new_size[1] // 2
    left = center_x - (new_width / 2)
    upper = center_y - (new_height / 2)
    right = center_x + (new_width / 2)
    lower = center_y + (new_height / 2)
    image = image.crop((left, upper, right, lower))
    return image


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
        # create image from numpy array
        animal_img = Image.fromarray(animal_array)
        # ensure array was converted to image
        if not isinstance(animal_img, Image.Image):
            print("Could not convert to Image")
            return

        # alter image to greyscale
        animal_img = ImageOps.grayscale(animal_img)
        # animal_img = animal_img.convert('L')

        # apply zoom and cropping to img
        zoom_factor = 1.25
        new_w = 400
        new_h = 400
        try:
            animal_img = ft_zoom(animal_img, zoom_factor, new_w, new_h)
            # print new array and its shape
            animal_array = array(animal_img)
            print(f"New shape after slicing: {animal_array.shape}")
            print(animal_array)

            # add border and scale
            border_width = 35
            animal_img = ImageOps.expand(animal_img, border=border_width,
                                         fill="white")
            animal_img = draw_scale(animal_img, border_width)

            animal_img.show()
        except Exception as e:
            print(f"An error occurred: {e}")
            return


if __name__ == "__main__":
    main()
