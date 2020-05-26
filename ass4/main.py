from math import sqrt
from ass4.animals import Animals, Cat         #modularity
from ass4.shapes import Shape, Square, Right_angled_triangle, Quadrilater

quad1 = Quadrilater()
quad1.set_width(5)
quad1.set_height(4)
print(quad1.area())

square= Square()
square.set_side(5)
print(square.area())