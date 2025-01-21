import math


class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__color = color
        # если кол-во сторон не равно то сторонами будет массив из 1 в количестве sides_count
        self.__sides = []

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *args):
        return len(args) == len(self.__sides) and all(isinstance(elem, int) for elem in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):

        if len(new_sides) == 1 and len(new_sides) == self.sides_count:
            if isinstance(new_sides[0], int):
                self.__sides.append(new_sides[0])
        elif len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color)
        __radius = int(sides / 2 * math.pi)

    def get_square(self):
        return len(self) ** 2 / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))



class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color)
        tuple_side = tuple(sides for x in range(self.sides_count))
        self.set_sides(*tuple_side)

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

print(len(circle1))
print(cube1.get_volume())
