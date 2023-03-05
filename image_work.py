from os import path
from PIL import Image


def get_filename():
    """
    Prompts the user for the file name of the image to be abstracted.

    Returns:
         (str): the name of the image that the user input
    """

    image_name = input("Enter the name of the image. Make sure that it is in the 'img' folder."
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
    row_step = int(total_size / root_num_tiles)
    column_step = int(row_step / root_num_tiles)

    image_rgb = []

    rows = 0

    while rows < total_size:
        to_add = []
        columns = 0

        while columns < row_step:
            to_add.append(rgb_values[rows + columns])
            columns += column_step

        image_rgb.append(to_add)
        rows += row_step

    return image_rgb