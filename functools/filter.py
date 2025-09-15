input_list = [3,4,5,6,7]


def is_even(num):
  return num % 2 == 0

result = filter(is_even, input_list)

print(list(result))