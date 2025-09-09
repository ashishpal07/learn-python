from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def speak(self):
    pass

class Cat(Animal):
  def speak(self):
    print("Meow")

cat = Cat()
cat.speak()

