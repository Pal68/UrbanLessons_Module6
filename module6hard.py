import math

class Figure:
    sides_count = 0
    def __init__(self, *args):
        self.__sides = []
        self.__color = []
        self.filled = False
        tmp_colors = args[0] #цвета
        tmp_sides = args[1:] #стороны
        self.set_color(tmp_colors[0], tmp_colors[1], tmp_colors[2])
        self.set_sides(*tmp_sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, red, green, blue):
        if red in range(0, 256) and green in range(0, 256) and blue in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        is_all_positive = all(num > 0 for num in new_sides)
        is_all_integer = (sum([num % 1 > 0 for num in new_sides]) == 0)
        if is_all_positive and is_all_integer:
            return True
        else:
            return  False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides) # если количество сторон в аргументе функции совпадает с sides_count
            else:
                if len(self.__sides) != self.sides_count:
                    self.__sides = [1] * self.sides_count #делаем список с единичными сторонами


class Circle(Figure):
    sides_count = 1
    def __init__(self, *args):
        super().__init__(*args)
        self.__radius = self.get_sides()[0]  / 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    def if_triangle_possible(self, args):
        a = args[0]
        b = args[1]
        c = args[2]
        if a + b > c and a + c > b and b + c > a:
            ret_val = True
        else:
            ret_val = False
        return ret_val

    def __init__(self, *args):
        if len(list(args[1: len(args)])) != 3:
            sides_list = [1, 1, 1]
        else:
            sides_list = list(args[1: len(args)])

        if self.if_triangle_possible(sides_list):
           super().__init__(*args)
           return
        else:
            raise ValueError("Нельзя построить треугольник с такими сторонами")

    def get_square(self):
        p = len(self) / 2
        tmp_sides = self.get_sides()
        return math.sqrt(p * (p - tmp_sides[0]) * (p - tmp_sides[1]) *(p - tmp_sides[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self, *args):
        super().__init__(*args)
        self.set_sides(*([args[1]] * 12))  #заполняем список сторон куба

    def get_volume(self):
        return (len(self) / self.sides_count) ** 3



# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


