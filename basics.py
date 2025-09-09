# variable string are dynamic
a = "hello"
b = 1
c = 1.5
a = 11

print(a)

# array / list
ar = [1,2,3,4,5]
for i in range(len(ar)):
  print(ar[i], end=" ")
print() 

# list comprehension
result = [x*x for x in ar]
print(result)

# matrix
matrix = []
for i in range(3):
  matrix.append([])
  for j in range(3):
    matrix[i].append(3)

print(matrix)

# other way 
other_matrix = [[0 for x in range(5)] for y in range(5)]
print(other_matrix)

# right angel triangle matrix
right_angel_matrix = [[0 for x in range(y+1)] for y in range(5)]
print(right_angel_matrix)

other_right_angel_matrix = []
for i in range(5):
  other_right_angel_matrix.append([])
  for j in range(i+1):
    other_right_angel_matrix[i].append(0)

print(other_right_angel_matrix)

# set
set = {1,2,3,4,5} # in python, set is collections of unique elements and sets are unordered collections of element
for ele in set:
  print(ele, end=" ")
print()

# dictionary
dict = {}
dict['a'] = 1
print(dict.get('b', 0))

# string
string = "hello"
for char in string:
  print(char)



