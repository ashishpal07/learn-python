# write a script in python that reads the file line by line and count total number of words
def count_words(filename):
  count = 0;
  with open("file.txt", "r") as f:
    for line in f:
      count += len(line.split())
    return count

print(count_words("file.txt"))


# Create a list comprehension to find all even numbers between 1 and 50.
ar = [x for x in range(1, 51) if x % 2 == 0]
print(ar)


# Implement a function that takes any number of arguments and returns their product.
def multiply(*args):
  res = 1
  for ele in args:
    res *= ele
  return res

product = multiply(1,5,2,4,5)
print(product)