from functools import reduce

list = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, list)
print(result)



def multiply(x, y):
  return x * y

product = reduce(multiply, list, 10)
print(product)