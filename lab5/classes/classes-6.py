
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

my_numbers = [2, 3, 4, 8, 9, 10, 11, 12]

prime_numbers = list(filter(lambda x: is_prime(x), my_numbers))

print("Prime Numbers:", prime_numbers)