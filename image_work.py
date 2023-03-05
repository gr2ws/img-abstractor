from os import path, mkdir


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


def make_spliced_img_dir(img_dir, img_name):
    """
    Creates the directory where the spliced images are to be stored, within the same directory as the image.

    Args:
         img_dir (str): default directory of the image.
         img_name (str): name of the image, used to name the directory.
    """

    dir_name = ""
    img_i = 0

    while img_name[img_i] != ".":
        dir_name += img_name[img_i]
        img_i += 1

    mkdir(f"{img_dir}\\{dir_name}")
