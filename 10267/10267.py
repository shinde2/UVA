import sys
from copy import deepcopy


image = None
region = None

def color_pixel(row, column, color):

    global image
    r =  row - 1
    c = column - 1

    image[r][c] = color


def clear_image():

    global image

    for r, row in enumerate(image):
        for c, column in enumerate(row):
            image[r][c] = "O"


def create_image(m, n):
    # m: columns, n: rows
    global image

    image = [["O" for _ in range(m)] for _ in range(n)]


def draw_vertical(row1, row2, column, color):

    global image

    r1 = row1 - 1
    r2 = row2 - 1
    c = column - 1

    for _r in range(r1, r2+1):
        image[_r][c] = color


def draw_horizontal(row, column1, column2, color):

    global image

    r = row - 1
    c1 = column1 - 1
    c2 = column2 - 1

    for _c in range(c1, c2+1):
        image[r][_c] = color


def fill_rectangle(row1, row2, column1, column2, color):

    global image

    for _r in range(row1, row2+1):
        draw_horizontal(_r, column1, column2, color)


def check_neighbour(r, c):

    global image
    global region

    R = len(image)
    C = len(image[0])
    color = image[r][c]
    coordinates = list()

    if 0 <= r-1 <= R-1:
        if 0 <= c-1 <= C-1:
            if image[r-1][c-1] == color and region[r-1][c-1] == 0:
                coordinates.append((r-1, c-1))
        if 0 <= c <= C-1:
            if image[r-1][c] == color and region[r-1][c] == 0:
                coordinates.append((r-1, c))
        if 0 <= c+1 <= C-1:
            if image[r-1][c+1] == color and region[r-1][c+1] == 0:
                coordinates.append((r-1, c+1))

    if 0 <= r <= R-1:
        if 0 <= c-1 <= C-1:
            if image[r][c-1] == color and region[r][c-1] == 0:
                coordinates.append((r, c-1))
        if 0 <= c+1 <= C-1:
            if image[r][c+1] == color and region[r][c+1] == 0:
                coordinates.append((r, c+1))

    if 0 <= r+1 <= R-1:
        if 0 <= c-1 <= C-1:
            if image[r+1][c-1] == color and region[r+1][c-1] == 0:
                coordinates.append((r+1, c-1))
        if 0 <= c <= C-1:
            if image[r+1][c] == color and region[r+1][c] == 0:
                coordinates.append((r+1, c))
        if 0 <= c+1 <= C-1:
            if image[r+1][c+1] == color and region[r+1][c+1] == 0:
                coordinates.append((r+1, c+1))

    return coordinates


def _fill_region(coordinates):

    global region

    if not coordinates:
        return
    else:
        for r, c in coordinates:
            region[r][c] = 1
            _fill_region(check_neighbour(r, c))


def fill_region(row, column, color):

    global image
    global region
    r = row - 1
    c = column - 1
    region = deepcopy(image)

    for _r, _row in enumerate(region):
        for _c, _column in enumerate(_row):
            region[_r][_c] = 0

    _fill_region([(r, c)])

    for _r, _row in enumerate(region):
        for _c, _column in enumerate(_row):
            if region[_r][_c] == 1:
                image[_r][_c] = color


def process_command(command):

    global image

    if command[0] == "I":
        create_image(command[1], command[2])
    if command[0] == "C":
        clear_image()
    if command[0] == "L":
        color_pixel(command[2], command[1], command[3])
    if command[0] == "V":
        draw_vertical(command[2], command[3], command[1], command[4])
    if command[0] == "H":
        draw_horizontal(command[3], command[1], command[2], command[4])
    if command[0] == "K":
        fill_rectangle(command[3], command[4], command[1], command[2], command[5])
    if command[0] == "F":
        fill_region(command[2], command[1], command[3])


def print_image():

    global image

    for r in image:
        for c in r:
            print(c, end="")
        print("")


def main():

    commands = [
        ["I", 5, 6],
        ["L", 2, 1, "G"],
        ["L", 1, 5, "Y"],
        ["V", 4, 2, 4, "B"],
        ["H", 1, 5, 2, "P"],
        ["K", 3, 5, 5, 6, "R"]
    ]

    for command in commands:
        process_command(command)

    print_image()
    print("--------------------")
    commands1 = [
        ["F", 2, 4, "Z"]
    ]

    for command in commands1:
        process_command(command)

    print_image()


if __name__ == '__main__':
    main()
