from math import sqrt
from ass3.animals import Animals, Cat
from ass3.shapes import Shape, Square, Right_angled_triangle

cat = Cat()  #defined cat class in another file and imported here
                #which lead to abstraction(not know what performed in function)

cat.__sound = 'Meeeeooooowwww'   #encapsulation as __sound is been used in def but this cant change the sound
print(cat.get_sound())

square = Square()

square.set_side(5)
print(square.area_wrt_s())
print(square.perimeter())

tri = Right_angled_triangle()
tri.set_height(3)
tri.set_width(4)
print(tri.get_hypoteneous())
