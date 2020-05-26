class Animals:
    __height = None
    __weight = None

    def set_weight(self,weight):
        self.__weight = weight

    def set_height(self,height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

class Dog(Animals):
    def __init__(self):
        self.__sound = "Barks"
        self.__lives = "Kennel"
        self.__kind = "Omnivores"
        self.__young = "Pub"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Cat(Animals):
    def __init__(self):
        self.__sound = "Meoww"
        self.__lives = "Kennel"
        self.__kind = "Carnivores"
        self.__young = "Kitten"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Cow(Animals):
    def __init__(self):
        self.__sound = "Moo"
        self.__lives = "Shed"
        self.__kind = "Herbivores"
        self.__young = "Calf"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Monkey(Animals):
    def __init__(self):
        self.__sound = "Hoops"
        self.__lives = "Tree"
        self.__kind = "Herbivores"
        self.__young = "Infant"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Lion(Animals):
    def __init__(self):
        self.__sound = "Roar"
        self.__lives = "Den"
        self.__kind = "Carnivores"
        self.__young = "Cub"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Horse(Animals):
    def __init__(self):
        self.__sound = "Neigh"
        self.__lives = "Stable"
        self.__kind = "Herbivores"
        self.__young = "Foal"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Donkey(Animals):
    def __init__(self):
        self.__sound = "Bray"
        self.__lives = "Shed"
        self.__kind = "Herbivores"
        self.__young = "Foal"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Rat(Animals):
    def __init__(self):
        self.__sound = "Squeak"
        self.__lives = "Hole"
        self.__kind = "Omnivores"
        self.__young = "Pups"

    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Rabbit(Animals):
    def __init__(self):
        self.__sound = "Squeak"
        self.__lives = "Burrow"
        self.__kind = "Herbivores"
        self.__young = "Kit"
    def get_sound(self):
        return self.__sound

    def get_lives(self):
        return self.__lives

    def get_kind(self):
        return self.__kind

    def get_youngones(self):
        return self.__young


class Goat(Animals):
    def __init__(self):
        self.__sound = "Bleat"
        self.__lives = "Shed"
        self.__kind = "Herbivores"
        self.__young = "Kid"

        def get_sound(self):
            return self.__sound

        def get_lives(self):
            return self.__lives

        def get_kind(self):
            return self.__kind

        def get_youngones(self):
            return self.__young


