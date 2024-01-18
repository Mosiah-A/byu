# word = "commitment"
# word_length = len(word)

# for i in range(word_length):
#     letter = word[i]
#     if letter == 'm':
#         print(letter.upper())
#     else:
#         print(letter)
#-------------------------------------------

# word = "commitment"
# word_length = len(word)

# favorite_letter= input("What's your favorite letter? ")
# for i in range(word_length):
#     letter = word[i]
#     if letter == favorite_letter.lower():
#         print(letter.upper(), end='')
#     else:
#         print(letter, end='')

#-----------------------------------

word = "commitment"
word_length = len(word)

favorite_letter= input("What's your favorite letter? ")
for i in range(word_length):
    letter = word[i]
    if letter == favorite_letter.lower():
        print("_", end='')
    else:
        print(letter, end='')
