from abc import ABC, abstractmethod

class Animal(ABC):     #abstract class          #interface as no concrete class here oly abstract class
    @abstractmethod
    def say(self):     #abstract method
        pass

dog = Animal()         #object cant be created of abstract class
dog.say()