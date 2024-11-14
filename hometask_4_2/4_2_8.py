from random import randint

'''Guess number! Program guessed num in range 0 to 100.
You have 8 attempts to guess it. If attempts are decreased - you lose.
Every attempt program tells you: bigger or smaller is guessed number than yours '''

attempts_count = 7
guessed_number = randint(0, 100)
attempt_counter = 1

while attempts_count >=0 :
    print(f'Attempt №{attempt_counter}:')
    a = int(input())
    if a < guessed_number:
        print('Wrong! Guessed number is bigger.')
        attempts_count -= 1
        attempt_counter += 1
    elif a > guessed_number:
        print('Wrong! Guessed number is smaller.')
        attempts_count -= 1
        attempt_counter += 1
    else:
        print("You win!")
        break