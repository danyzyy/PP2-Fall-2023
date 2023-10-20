def spy_game(numbers):
    for i in range(len(numbers) - 2):
        if numbers[i] == 0 and numbers[i + 1] == 0 and numbers[i + 2] == 7:
            return True
    return False

test_list = [7, 8, 3, 0, 2, 1, 5]

if spy_game(test_list):
    print("True")
else:
    print("False")