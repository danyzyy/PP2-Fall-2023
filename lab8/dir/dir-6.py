for ascii_value in range(ord('A'), ord('Z') + 1):
    file_name = "{}.txt".format(chr(ascii_value))
    file_handle = open(file_name, "x")
