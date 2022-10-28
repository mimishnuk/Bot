class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    p = 3.1415

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return round(self.p * (self.__radius ** 2), 2)

    def info(self):
        return f'Circle radius: {self.__radius}  Area: {self.calculate_area()}'


class RightTriangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round(1/2 * (self.__side_a * self.__side_b), 2)


    def info(self):
        return f'RightTriangle side a: {self.__side_a} side b: {self.__side_b} area: {self.calculate_area()}  '


def create_figures():
    circle = Circle(4)
    circle2 = Circle(6)
    triangle1 = RightTriangle(15, 16)
    triangle2 = RightTriangle(10, 7)
    triangle3 = RightTriangle(8, 6)
    figures = [circle, circle2, triangle1, triangle2, triangle3]
    return figures

brain = create_figures()

for i in brain:
    print(i.info())







