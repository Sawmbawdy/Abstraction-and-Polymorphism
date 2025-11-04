from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I can walk and run")

class Snake(animal):
    def move(self):
        print("I can slither around")

class Fish(animal):
    def move(self):
        print("I can swim")

class Bird(animal):
    def move(self):
        print("I can fly")

R = Human()
R.move

K = Snake()
K.move()

J = Fish()
J.move()

A = Bird()
A.move()
