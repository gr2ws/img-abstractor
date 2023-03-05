from image_work import *

# PROCURE IMAGE
img_default = "img"
img_name = get_filename()

while not image_exist(img_default, img_name):
    print(f"Image not found! Please make sure it is in the '{img_default}' folder and that the file name is correct.")
    img_name = get_filename()

img_loc = f"{img_default}\\{img_name}"

make_spliced_img_dir(img_default, img_name)