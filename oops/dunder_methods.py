class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Person({self.name})"
  
  def __repr__(self):
    return f"Person({self.name})"
  
  def __add__(self, other):
    return Person(self.name + " " + other.name)
  
  def __len__(self):
    return len(self.name)
  
  def __eq__(self, other):
    return self.name == other.name
  

p1 = Person("John")
p2 = Person("Doe")

print(p1) # calls __str__
print(repr(p2)) # calls __repr__
print(p1 == p2) # calls __eq__
p3 = p1 + p2 # calls __add__
print(p3)
print(len(p3)) # calls __len__