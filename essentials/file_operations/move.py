import os

source = "public/copied"
destintaion = f"/Users/markinger/Desktop/{source.split('/')[-1]}"

try:
    if os.path.exists(destintaion):
        print("There is already a file within this destination path")
    else:
        os.replace(source, destintaion)

        try:
          with open(destintaion, "a") as moved_file:
              moved_file.write(f"\n\nThis file was moved from {source} here :)")
        except Exception:
            print("Couldn't add text to moved element (if it is a directory, then it's OK)")
except FileNotFoundError as e:
    print(f"File at path {source} wasn't found.")