from math import sqrt

class Shape:
    pass

class Circle(Shape):

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return 3.14* self.get_radius() * self.get_radius()

    def perimeter(self):
        return 2*3.14* self.get_radius()

class Triangle(Shape):
    __width = None
    __height = None

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.get_width() * self.get_height() / 2

class Right_angled_triangle(Triangle):
    def get_hypoteneous(self):
        a = self.get_height()* self.get_height()
        b= self.get_width()* self.get_width()
        return sqrt(a+b)

class Equilateral_triangle(Triangle):
    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def perimeter(self):
        return (3 * self.get_side())

class Isosceles_triangle(Triangle):

    def set_equalside(self, side):
        self.__side = side

    def get_equalside(self):
        return self.__side

    def set_base(self, base):
        self.__base = base

    def get_base(self):
        return self.__base

    def perimeter(self):
        return (2*self.get_equalside())+self.get_base()

class Quadrilater(Shape):
    __width = None
    __height = None

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area_wrt_hw(self):
        return self.get_width() * self.get_height()

class Square(Quadrilater):

    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def area_wrt_s(self):
        return self.get_side()*self.get_side()

    def perimeter(self):
        return 4* self.get_side()

class Rectangle(Quadrilater):

    def perimeter(self):
        return 2 * (self.get_height() + self.get_width())

class Rhombus(Quadrilater):
    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def area_wrt_s(self):
        return self.get_side() * self.get_side()

    def perimeter(self):
        return 4 * self.get_side()

class Parallelogram(Quadrilater):
    def set_side(self, side):
        self.__side = side

    def get_side(self):
        return self.__side

    def set_base(self, base):
        self.__base = base

    def get_base(self):
        return self.__base

    def perimeter(self):
        return 2 * (self.get_side() + self.get_base())