ar = [1,2,3,4,5]


for i, val in enumerate(ar):
  print(i, val, end=" -> ")
print()

ar2 = [4,5,6]
for x, y in zip(ar, ar2):
  print(x, y, end=" -> ")
print()

print(all([True, False]))
print(any([False,True, True]))





