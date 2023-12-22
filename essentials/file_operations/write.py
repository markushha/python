# write a file

with open('public/write.txt', 'w') as file:
  file.write('Hello File!\nJust some text. Make sure, that if you will run this again, it will overwrite the very same file with new string!')

# how to append new changes to a file (not overwrite)

with open('public/write.txt', 'a') as file:
  file.write("\n\nThis text just appeared using append!")