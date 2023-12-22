import os

# file detection

path = "/Users/markinger/Code/python/public/brief.txt"
dir = "/Users/markinger/Documents/sat"

def check_path(path):
  if os.path.exists(path):
    if (os.path.isfile(path)):
      print("it's a file!")
    elif os.path.isdir(path):
      print("it's a directory!")
  else:
    print("path isn't valid")

# check_path(path)
# check_path(dir)

# read a file

try:
  with open(path) as file:
    print(file.read())
except UnicodeDecodeError as e:
  print("You must provide utf-8 format (.txt, .html, .md). You can't provide any images (.png, .jpg, etc.)")
except FileNotFoundError:
  print("Error: file not found. Please, correct your path and make sure it's available.")
except Exception as e:
  print(f"Something went wrong. Error message: {e}")


