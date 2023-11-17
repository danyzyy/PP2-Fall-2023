
file_a_content = open(r"/Users/Asus/Desktop/pp2/lab8/row.txt").read()
file_b_content = open("/Users/Asus/Desktop/pp2/lab6/sample-data.json").read()
file_c = open(r"/Users/Asus/Desktop/pp2/lab8/row.txt")
file_d = open("/Users/Asus/Desktop/pp2/lab6/sample-data.json")
file_e_content = open("all.txt").read()

if file_e_content:
    print(file_e_content.count("\n") + 1)
else:
    print(file_e_content.count("\n"))
print("Counting lines using the count() method:")
print(file_a_content.count("\n") + 1)
print(file_b_content.count("\n") + 1)
print("Counting lines using readlines() method:")
print(len(file_c.readlines()))
print(len(file_d.readlines()))
