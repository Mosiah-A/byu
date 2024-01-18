number_1 = int(input('What is the fisrt number? '))
number_2 = int(input('What is the second number? '))

if number_1 > number_2:
    print('The first number is greater')
else:
    print('The first number is not greater')
if number_1 == number_2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')
if number_2 > number_1:
    print('The second number is greater')
else: 
    print('The second number is not greater')

print('')

favorite_animal = input('What is your favorite animal? ')

if favorite_animal.lower() == 'bear':
    print("That's my favorite animal too!")
else:
    print('That one is not my favorite.')