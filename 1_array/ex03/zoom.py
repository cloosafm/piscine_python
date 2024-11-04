from PIL import Image, ImageOps, ImageDraw, ImageFont
from load_image import ft_load

"""
This program loads an image, prints some info, modify the image, displays it.
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


def main():
    """
    Calls the ft_load() function to show the image info
    Makes alterations
    Shows info post-alterations
    Displays image
    """
    animal_array = ft_load("animal.jpeg")
    if animal_array is not None:
        print(animal_array)
        animal_img = Image.fromarray(animal_array)
        animal_img = ImageOps.grayscale(animal_img)

        # apply zoom to img
        zoom_factor = 1.25
        width, height = animal_img.size
        new_size = (int(width * zoom_factor), int(height * zoom_factor))
        animal_img = animal_img.resize(new_size, Image.Resampling.BICUBIC)

        # crop to desired size
        center_x, center_y = new_size[0] // 2, new_size[1] // 2
        new_width = 400
        new_height = 400
        left = center_x - (new_width / 2)
        upper = center_y - (new_height / 2)
        right = center_x + (new_width / 2)
        lower = center_y + (new_height / 2)
        animal_img = animal_img.crop((left, upper, right, lower))

        # save and load altered image
        animal_img.save("zoomed_in_image.jpeg")
        new_animal_img = ft_load("zoomed_in_image.jpeg")
        print(new_animal_img)
        new_animal_img = Image.fromarray(new_animal_img)

        # Add a white border and a scale
        border_width = 35
        new_animal_img = ImageOps.expand(new_animal_img, border=border_width,
                                         fill="white")
        new_animal_img = draw_scale(new_animal_img, border_width)

        new_animal_img.show(title="Tadaa!")


if __name__ == "__main__":
    main()
