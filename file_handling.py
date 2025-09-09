with open("file.txt", "w") as f:
  f.write("file handling with python write mode")

with open("file.txt", "r") as f:
  print(f.read())

with open("file.txt", "w") as f:
  f.write("file handling with python write")

with open("file.txt", "a") as f:
  f.write("\nfile handling with python append mode")

