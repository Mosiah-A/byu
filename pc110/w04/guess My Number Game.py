import random
play_again = 'y'
while play_again.lower() == 'y':
    number = random.randint(1, 10)
    guess = int(input("What is the number? "))
    count  = 1
    while guess != number:
        if guess > number:
            print("It's Lower")
            guess = int(input("What is the number? "))
            count  = count + 1
        elif guess < number:
            print("It's higher")
            guess = int(input("What is the number? "))
            count  = count + 1
    print(f'Congratulation the number was {number}')
    print(f"You guess {count} times")
    play_again = input("do you wanto to play again? (Y/N) \n ")
print('END GAME')
