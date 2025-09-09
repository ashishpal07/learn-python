class Animal:
  def speak(self):
    print("Animal speaks")

class Dog(Animal): # inheritance
  def bark(self):
    print("Dog barks")

dog1 = Dog()
dog1.speak() # inherited method
dog1.bark() # own method

# Method overriding
class Cat(Animal):
  def speak(self):
    print("cat meows")

cat1 = Cat()
cat1.speak() # overridden method

# super() function
class Bull(Animal):
  def speak(self):
    super().speak() # calling parent class method
    print("Bull roars")

bull = Bull()
bull.speak()


# Multiple Inheritance
class Father:
  def skills(self):
    print("Gardening")

class Mother:
  def skills(self):
    print("Cooking")

class Child(Mother, Father):
  def skills(self):
    Father.skills(self)
    Mother.skills(self)
    print("sports")

child = Child()
child.skills()

# MRO (Method Resolution Order): Python follows the c3 linearization algorithm to determines the
# which method to call when there are multiple inheritance.
# print(Child.mro())

# super() with multiple inheritance
class A:
  def show(self):
    print("A")
  
class B(A):
  def show(self):
    super().show()
    print("B")

class C(A):
  def show(self):
    super().show()
    print("C")

class D(B, C):
  def show(self):
    super().show()
    print("D")

d = D()
d.show()
# print(D.mro())

# Method overriding 
class Parent:
  def display(self):
    print("parent display")

class child(Parent):
  def display(self):
    print("child display")

def make_people_display(obj):
  obj.display()
  
make_people_display(Parent())
make_people_display(child())

