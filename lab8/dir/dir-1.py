import os

root_directory = r"C:\Users\Asus\Desktop\pp2"


with open("directory.txt", "x") as directory_file:
    directory_file.write("List of only directories:\n")
    for current_path, subdirectories, _ in os.walk(root_directory):
        for directory_name in subdirectories:
            directory_file.write(directory_name + "\n")

with open("files.txt", "x") as files_file:
    files_file.write("List of only files:\n")
    for current_path, _, filenames in os.walk(root_directory):
        for file_name in filenames:
            files_file.write(file_name + "\n")

with open("all.txt", "x") as all_file:
    all_file.write("List of all directories and files:\n")
    for current_path, subdirectories, filenames in os.walk(root_directory):
        for file_name in filenames:
            all_file.write(os.path.join(current_path, file_name) + "\n")
