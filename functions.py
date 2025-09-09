def add(a, b):
  return a + b

sum = add(1, 3) # this will not give you error but this is not a good practice
print(sum)

# *args and **kwargs
def do_something(*args):
  print(type(args))
  for ele in args:
    print(ele)

do_something("a", "b", "c")

do_something("a", [1,2,3], "d")

def kwargs_implement(**kwargs):
  print(type(kwargs))
  print(kwargs)
  for ele in kwargs:
    print(kwargs[ele])

kwargs_implement(a="image", b="defame", c="swagger")

  


