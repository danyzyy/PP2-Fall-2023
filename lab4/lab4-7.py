x = int(input())
numbers = set(range(1, x + 1))
possibl = numbers
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possibl &= guess
    else:
        possibl &= numbers - guess

print(' '.join([str(x) for x in sorted(possibl)]))
