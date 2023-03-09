from os import path
from PIL import Image


def get_filename():
    """
    Prompts the user for the file name of the image to be abstracted.

    Returns:
         (str): the name of the image that the user input.

    """

    image_name = input("Enter the name of the image. Make sure that it is in the 'img' folder."
                       "\nMake sure that the img folder is in the same directory/folder as this file."
                       "\nInclude the file type (img.png, img.jpeg, etc.): ")
    return image_name


def image_exist(img_folder, img_name):
    """
    Determines if the image exists inside the img directory.

    Args:
        img_folder (str): the default image folder.
        img_name (str): name of the file.

    Returns:
        (bool): True if exists, otherwise False
    """

    return path.exists(f"{img_folder}\\{img_name}")


def get_pixels(img_loc, root_num_tiles):
    """
    Gets a tiles x tiles size 2d array representing the rgb values of a specific (x, y) point in an image.
    Divides the image evenly into the user desired number of tiles, sampling a point using said number as an increment.
    The total number of tiles is the root_num_tiles ^ 2.

    Args:
        img_loc (str): the relative path of the image.
        root_num_tiles (int): the number of tiles to be painted by row, for a number of times.
    Returns:
        A root_num_tiles x root_num_tiles 2d array representing a plane, each point having tuple (r, g, b) values.
    """

    img = Image.open(img_loc)

    rgb_values = list(img.getdata())
    total_size = len(rgb_values)
    height, width = img.height, img.width
    flat_row = 0

    unflatten_rgb = []

    while flat_row < total_size:
        to_add = []
        flat_column = 0
        while flat_column < width:
            to_add.append(rgb_values[flat_row + flat_column])
            flat_column += 1
        unflatten_rgb.append(to_add)
        flat_row += width

    paint_rgb = []
    y_step = int(height / root_num_tiles)
    x_step = int(width / root_num_tiles)

    paint_row = 0

    while paint_row < height:
        paint_column = 0
        to_add = []
        while paint_column < width:
            to_add.append(unflatten_rgb[paint_row][paint_column])
            paint_column += x_step
        paint_rgb.append(to_add)
        paint_row += y_step

    return paint_rgb


def get_ascii(img_loc, line_length, mode, text):
    """
        Gets an array of lines filled with ascii symbols, chosen based on the perceived brightness of the color at a
        specific tile in a specific coordinate in the image.

        Args:
            img_loc (str): the relative path of the image.
            line_length(int): the number of lines to be outputted by row, for a number of times.
            mode (str): to make ASCII art or to use text.
            text (str): the text to be looped over and over again for text mode only.
        Returns:
            An array of lines, to be printed sequentially to view the product.
        """

    img = Image.open(img_loc)

    rgb_values = list(img.getdata())
    total_size = len(rgb_values)
    height, width = img.height, img.width
    flat_row = 0

    unflatten_rgb = []

    while flat_row < total_size:
        to_add = []
        flat_column = 0
        while flat_column < width:
            to_add.append(rgb_values[flat_row + flat_column])
            flat_column += 1
        unflatten_rgb.append(to_add)
        flat_row += width

    def get_luminance_scale(r, g, b):
        return int(round((0.299 * r + 0.587 * g + 0.114 * b) / 25, 0)) - 1

    ascii_chars = [" ", "~", ":", "*", "#", "▒", "▓", "▓", "█", "█"]
    ascii_row = 0
    ascii_output = []

    color_flags = ["238", "242", "247",  "250", "253"]

    text_counter = 0
    text_length = len(text)

    y_step = int(height / line_length)
    x_step = int(width / line_length)

    while ascii_row < height:
        ascii_column = 0
        to_add = ''

        while ascii_column < width:
            luminance = get_luminance_scale(unflatten_rgb[ascii_row][ascii_column][0],
                                            unflatten_rgb[ascii_row][ascii_column][1],
                                            unflatten_rgb[ascii_row][ascii_column][2])
            if mode == "ascii":
                to_add += f"{ascii_chars[luminance]}{ascii_chars[luminance]}{ascii_chars[luminance]}"

            elif mode == "text":
                text_index = 0

                if text_counter > 0:
                    text_index = (text_counter % text_length) - 1

                to_add += f"\033[38;5;{color_flags[int((luminance + 1) / 2) - 1]}m" \
                          f"{text[text_index]}" \
                          f"{text[text_index + 1 - text_length]}" \
                          f"{text[text_index + 2 - text_length]}"

                to_add = f"{to_add}"
                text_counter += 3

            ascii_column += x_step

        ascii_output.append(to_add)
        ascii_row += y_step

    return ascii_output
