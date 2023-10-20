def is_palindrome(text):
    clean_text = ''.join(text.split()).lower()
    return clean_text == clean_text[::-1]

test_cases = ["qazaq", "Denmark"]

for test_case in test_cases:
    if is_palindrome(test_case):
        print(f'"{test_case}" is a palindrome.')
    else:
        print(f'"{test_case}" is not a palindrome.')