from image_work import *

# PROCURE IMAGE
img_default = "img"
img_name = get_filename()

while not image_exist(img_default, img_name):
    print("Image not found! Please make sure it is in the img folder and that the file name is correct.")
    img_name = get_filename()

img_directory = f"{img_default}\\{img_name}"

# MAKE IMAGE 1:1
