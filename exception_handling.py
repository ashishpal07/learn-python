try:
  print("start")
  result = 10 / 0
except Exception as e:
  raise Exception("exception raised") from e
finally:
  print("bhai apna kaam karo")


