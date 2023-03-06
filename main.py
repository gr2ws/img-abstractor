from image_work import *
from turtle import Turtle, Screen

# PROCURE IMAGE
img_default = "img"
img_name = 'def'

while not image_exist(img_default, img_name):
    img_name = get_filename()

img_loc = f"{img_default}\\{img_name}"

mode = input("ASCII: Darkness and lightness will be represented by different ASCII characters."
             "\nPaint: A Python Turtle will paint an abstractized image for you."
             "\nText: Loop a line of text, with capitalization representing darkness and lightness."
             "\n(ASCII / Paint / Text): ").lower()

if mode == "paint":
    available_num_tiles = [16, 32, 64, 128, 256, 512, 640]

    tiles_index = int(input("Enter the desired resolution of the image: "
                            "\n1 - 16 x 16\n2 - 32 x 32\n3 - 64 x 64"
                            "\n4 - 128 x 128\n5 - 256 x 256\n6 - 512 x 512"
                            "\n7 - Max Canvas Size (640 x 640)\nSize: ")) - 1

    root_num_tiles = available_num_tiles[tiles_index]

    # READY CANVAS
    max_canvas_height, max_canvas_width = 640, 640
    canvas = Screen()
    canvas.screensize(max_canvas_height, max_canvas_width)
    row_step, column_step = int(max_canvas_height / root_num_tiles), int(max_canvas_width / root_num_tiles)
    canvas.colormode(255)

    # READY TURTLE
    available_sizes = [1.6, .8, .4, .35, .3, .2, .1]

    painter = Turtle()
    painter.resizemode("auto")
    turtle_size = available_sizes[tiles_index]
    painter.shapesize(turtle_size, turtle_size, turtle_size)
    painter.hideturtle()
    painter.shape(input("Enter turtle shape (circle, square, triangle, arrow, turtle): "))
    painter.speed(0)

    # PAINT
    start_height, start_width = -(int(max_canvas_height / 2)), -(int(max_canvas_height / 2))

    row = 0
    paint_row = 0

    painter.penup()
    painter.goto(start_height, start_width)

    image_rgb = get_pixels(img_loc, root_num_tiles)

    while paint_row < root_num_tiles:
        column = 0
        paint_column = 0

        while paint_column < root_num_tiles:
            print(f"{image_rgb[paint_row][paint_column]} @ ({paint_row}, {paint_column})")

            painter.goto(start_width + column, start_height + row, )
            painter.stamp()
            painter.color(image_rgb[root_num_tiles - 1 - paint_row][paint_column])

            paint_column += 1
            column += column_step

        paint_row += 1
        row += row_step

    canvas.exitonclick()
elif mode == "ascii" or "text":
    available_line_size = [16, 32, 64, 128]

    if mode == "text":
        text = input("Warning! Text mode is fixed to 64 line length."
                     "\nEnter a sentence/sentences.\n")
        lines_index = 2
    else:
        lines_index = int(input("Enter the desired line length: "
                                "\n1 - 16 x 16\n2 - 32 x 32\n3 - 64 x 64"
                                "\n4 - 128 x 128\nSize: ")) - 1
        text = ""

    image_ascii = get_ascii(img_loc, available_line_size[lines_index], mode, text)

    for line in image_ascii:
        print(line, end="\n")
