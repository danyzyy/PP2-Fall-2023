import os

file_path = r"/Users/Asus/Desktop/pp2/lab8/row.txt"
if os.path.exists(file_path):
    print("The path exists!")
else:
    print("The path does not exist :(")
with open(file_path, 'r') as file:
    print(f"Readable: {file.readable()}")
    print(f"Writable: {file.writable()}")
if os.access(file_path, os.X_OK):
    print("The file is executable!")
else:
    print("The file is not executable.")
