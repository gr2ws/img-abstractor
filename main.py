from os import path
from get_img import *
# GET THE FILE

img_default = "img"
img_name = get_image()

while not image_exist(img_default, img_name):
    print("Image not found! Please make sure it is in the img folder and that the file name is correct.")
    img_name = get_image()

img_directory = f"{img_default}\\{img_name}"
