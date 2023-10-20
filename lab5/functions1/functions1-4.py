def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers_str):
    numbers = [int(num) for num in numbers_str.split()]
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers
