from image_work import *
from turtle import Turtle, Screen

# PROCURE IMAGE
img_default = "img"
img_name = get_filename()
root_num_tiles = 16  # since image is 1:1, one size for width and height of the painting

while not image_exist(img_default, img_name):
    print(f"Image not found! Please make sure it is in the '{img_default}' folder and that the file name is correct.")
    img_name = get_filename()

img_loc = f"{img_default}\\{img_name}"

# GET RGB VALUES
image_rgb = get_pixels(img_loc, root_num_tiles)

# READY CANVAS
max_canvas_height, max_canvas_width = 512, 512
canvas = Screen()
canvas.screensize(max_canvas_height, max_canvas_width)
row_step, column_step = int(max_canvas_height / root_num_tiles), int(max_canvas_width / root_num_tiles)
canvas.colormode(255)

# READY TURTLE
painter = Turtle()
painter.resizemode("auto")
painter.shapesize(.5, .5, .5)
painter.shape("circle")
painter.speed(0)

# PAINT
start_height, start_width = (int(max_canvas_height / 2)), (int(max_canvas_height / 2))

row = 0
paint_row = 0

painter.penup()
painter.goto(start_height, start_width)
painter.hideturtle()

while paint_row < root_num_tiles:
    column = 0
    paint_column = 0
    while paint_column < root_num_tiles:
        print(paint_row, paint_column)
        painter.color(image_rgb[paint_row][paint_column])
        painter.goto(start_width - column, start_height - row,)
        painter.stamp()
        paint_column += 1
        column += column_step
    paint_row += 1
    row += row_step

canvas.exitonclick()