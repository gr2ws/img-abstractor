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


def get_coordinate_step(img_loc, samples_per_row):
    """
    Gets the step for each next coordinate to be sampled.

    Args:
        img_loc (str): location of the image
        samples_per_row (int): how many times each row of an image should be sampled

    Returns:
        (int): the int step, rounded down
    """
    img = Image.open(img_loc)
    step = int(img.size[0] // samples_per_row)

    return step

