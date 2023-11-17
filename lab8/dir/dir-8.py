import os
file_path = r"/Users/Asus/Desktop/pp2/lab8/A.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The file does not exist.")
