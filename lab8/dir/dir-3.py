import os
file_path = "/Users/Asus/Desktop/pp2/lab8/row.txt"
if os.path.exists(file_path):
    file_name = os.path.basename(file_path)
    file_directory = os.path.dirname(file_path)

    print(f"File Name: {file_name}")
    print(f"Path to File: {file_directory}")
else:
    print("The path does not exist.")
