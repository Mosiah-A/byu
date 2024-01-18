'''
Author: Mosiah andrade

Purspose: Wordle game
'''
#secret word
secret_word = 'mosiah'

#variables
word_lenght = len(secret_word)
guess = '_' * word_lenght
guess_lenght = len(guess)
count = 0


while guess != secret_word:

    #valid the answer
    while guess_lenght != word_lenght:
        print('Sorry, the guess must have the same number of letters as the secret word.')
        guess = input(' \nWhat is your guess? ')
        guess_lenght = len(guess)
        count = count + 1


    print('Your hint is: ', end='')

    for index in range(word_lenght):
            
        guess_letter = guess[index]
        secret_letter = secret_word[index]

        #if the letter is in the right place
        if guess_letter == secret_letter:
            print(secret_letter.upper(), end='')
        else:
            #if the letter is in the wrong place
            if guess_letter in secret_word:
                print(guess_letter.lower(), end='')
            
            #if don't have the letter
            else:
                print('_', end='')
    
    #input a new guess
    guess = input(' \nWhat is your guess? ')
    guess_lenght = len(guess)
    geess = guess.lower()
    count = count + 1 #Couting the point

    #couting life
    if count >= 5 and guess != secret_word: 
        print('GAME OVER')
        break #to quit the loop
if count >= 5 and guess != secret_word:
    print(    )
else:
    print('Congratulations! You guessed it!')
    print(f'It took {count} guesses')