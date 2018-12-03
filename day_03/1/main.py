import re


class Shape:
    def __init__(self, identifier, left_coord, top_coord, width, height):
        self.identifier = identifier
        self.left_coord = left_coord
        self.top_coord = top_coord
        self.width = width
        self.height = height


def create_shape(string_notation):
    shape_information = re.split('#|@ |: ', string_notation)
    coords = re.split(',', shape_information[2])
    size = re.split('x', shape_information[3])
    return Shape(
        int(shape_information[1]),
        int(coords[0]),
        int(coords[1]),
        int(size[0]),
        int(size[1])
    )


shapes = open("./1.input", "r").read().splitlines()

matrix = {}
for shape in shapes:
    shapeObject = create_shape(shape)

    x_coords = range(shapeObject.left_coord, shapeObject.left_coord + shapeObject.width)
    y_coords = range(shapeObject.top_coord, shapeObject.top_coord + shapeObject.height)

    for x in x_coords:
        for y in y_coords:
            if x in matrix:
                if y in matrix[x]:
                    matrix[x][y] += 1
                else:
                    matrix[x].update({y: 1})
            else:
                matrix.update({x: {}})
                matrix[x].update({y: 1})

duplicates = 0
for ind_x, x in matrix.items():
    for ind_y, y in x.items():
        if y > 1:
            duplicates += 1

print(duplicates)
