class Point:
    def __init__(self, x, y):
        self.x = X
        self.y = y


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height
        ending_point_x = self.starting_point.x + self.width
        ending_point_y = self.starting_point.y + self.height
        self.ending_point = Point(ending_point_x, ending_point_y)

    def area(self):
        return self.width * self.height

    def print_area(self):
        print(self.area())

    def print_start_and_end_points(self):
        print("Starting Point (X)): " + str(self.starting_point.x))
        print("Starting Point (Y)): " + str(self.starting_point.y))
        print("End Point X-Axis (Top Right): " + str(self.ending_point.x))
        print("End Point Y-Axis (Bottom Left): " + str(self.ending_point.y))


def create_rectangle():
    rectangle_starting_point = Point(50, 100)
    rectangle = Rectangle(rectangle_starting_point, 90, 10)
    return rectangle


rectangle = create_rectangle()

print(rectangle.area())
rectangle.print_start_and_end_points()
