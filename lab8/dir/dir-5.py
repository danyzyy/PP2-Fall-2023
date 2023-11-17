
lines_from_a = open(r"/Users/Asus/Desktop/pp2/lab8/row.txt").readlines()
with open("files.txt", "a") as output_file:
    for line in lines_from_a:
        output_file.write(line)
    output_file.write("\n")
updated_content = open("files.txt").read()
print(updated_content)
