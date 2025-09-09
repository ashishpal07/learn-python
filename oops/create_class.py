class Dog:
  def __init__(self, name, age): # constructor
    self.name = name # instance variable
    self.age = age # instance variable


dog1 = Dog('labrador', 5)

print(dog1.name)
print(dog1.age)


class Car:
  wheels = 4 # class variable

  def __init__(self, name, color):
    self.name = name 
    self.color = color

  def start(self):
    print(f"{self.name} car is starting")

car1 = Car('BMW', 'Black')
print(car1.name, car1.color, car1.wheels)
