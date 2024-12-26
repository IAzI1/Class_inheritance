class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__sides = []
        self.__color = color
        field = True

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        for value in (r, g, b):
            if value > 255 or value < 0:
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b
