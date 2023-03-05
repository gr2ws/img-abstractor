from image_work import *

# PROCURE IMAGE
img_default = "img"
img_name = get_filename()
tiles_per_row = 256  # since image is 1:1, one size for width and height

while not image_exist(img_default, img_name):
    print(f"Image not found! Please make sure it is in the '{img_default}' folder and that the file name is correct.")
    img_name = get_filename()

img_loc = f"{img_default}\\{img_name}"