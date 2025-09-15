from functools import reduce
from itertools import accumulate

input_list = [3,4,5,6]

result = accumulate(input_list, lambda x, y: x + y, 10)
print(list(result))