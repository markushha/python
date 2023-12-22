import shutil, os

# copyfile() - to copy a file
# copy() - to copy not only a file but also a dir (permission mode)
# copy2() - same as copy but with metadata (file's creation and modification times)

copy_from = 'public/write.txt'
copy_to = 'public/copied/copy-of-write.txt'

# before copying, I will create a "copied" directory

os.mkdir("public/copied")

shutil.copyfile(copy_from, copy_to)

with open(copy_to, 'a') as file:
    file.write(f"\nThis file was copied from {copy_from}")