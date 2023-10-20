def uni_el(newlist):
    return [item for item in newlist if newlist.count(item) == 1]

newlist = [1, 2, 2, 3, 4, 4, 5]
result = uni_el(newlist)
print(result)