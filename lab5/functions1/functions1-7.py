def has_33(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False


print(has_33([1, 3, 3]))       
print(has_33([1, 3, 1, 3]))   
print(has_33([3, 1, 3]))       
