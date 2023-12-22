import os, shutil

# firsly, I'll create a simple and filder file which then I'll delete

file_path = "public/simple.txt"
dir_path = "public/empty"
dir_with_files_path = "public/files_folder"

# creating the files and folders

with open(file_path, "w") as new_file:
  new_file.write("I will be deleted very soon :(")

os.mkdir(dir_path)
os.mkdir(dir_with_files_path)

with open(f"{dir_with_files_path}/some.txt", "w") as new_file:
  new_file.write("Hello?")

# deleting

try:
  os.remove(file_path) # to remove a file
  os.rmdir(dir_path) # for EMPTY folders 
  shutil.rmtree(dir_with_files_path) # for folders that DO contain files
except FileNotFoundError:
  print("File you're trying to delete doesn't exist!")
except PermissionError:
  print("Permission wasn't granted")
except Exception as e:
  print(f"Something went wrong. Specification: {e}")
finally:
  print(f"Empty directory {dir_path} was removed.\nDirectory with files {dir_with_files_path} was removed.\nFile {file_path} was removed.")