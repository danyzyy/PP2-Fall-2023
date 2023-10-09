a = int(input())
numbers = set(range(1, a + 1))
possibl = numbers
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    if len(possibl & guess) > len(possibl) / 2:
        print('YES')
        possibl &= guess
    else:
        print('NO')
        possibl &= numbers - guess
        
print(' '.join([str(x) for x in sorted(possibl)]))
