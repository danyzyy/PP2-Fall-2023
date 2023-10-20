import random

print('Hello! What is your name?')
player_name = input()

print(f'Well, {player_name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')

random_number = random.randint(1, 20)

def too_low():
    print('Your guess is too low')
    print('Take a guess.')

def too_high():
    print('Your guess is too high.')
    print('Take a guess.')

guess_count = 1
while True:
    user_guess = int(input())
    if user_guess == random_number:
        print(f'Good job, {player_name}! You guessed my number in {guess_count} guesses!')
        break
    if user_guess < random_number:
        too_low()
    if user_guess > random_number:
        too_high()
    guess_count += 1