from os import path


def get_image():
    """
    Gets the file name of the image to be abstracted.

    Returns:
        image_name(str) - name of the image
    """

    image_name = input("Enter the name of the image. Make sure that it is in the 'img' folder."
                       "\nInclude the file type (img.png, img.jpeg, etc.): ")
    return image_name


def image_exist(img_folder, img_name):
    """
    Determines if the image exists inside the img directory .

    Parameters:
        img_folder(str) - the default image folder.
        img_name(str) - name of the file.

    Returns:
        (bool) - True if it does, False if not
    """

    return path.exists(f"{img_folder}\\{img_name}")