# tip = float(input("What is the tip amount? "))

# while tip < 0:
#     print("Sorry, the tip cannot be negative")
#     tip = float(input("What is the tip amount? ")) #it's necessary to don't fall in eternal loop
#     #Jump back up to line 3 while line 3 is True
    
# print(f"You have tipped an amount of {tip:.2f}")


# ------------------------------------------------------
# number = 0 
# name = ""
# while number < 10:
#     number = int(input("What is the number? "))
#     name = input('what is you name? ')

# print(f'your name is: {name}')

# ------------------------------------------------

# number = int(input("Please type a positive number: "))

# while number <= 0 :
#     print('Sorry, that is a negative number. Please try again')
#     number = int(input("Please type a positive number: "))

# print(f'The number is {number}')

#--------------------------------------------------------

# answer = ""

# while answer.lower() != "yes":
#     answer = input("May I have a piece of candy? ")

# print("Thank you.")

#------------------------------------------------------

# names = ['Mosiah', 'Andrade']
# index = 0
# while index < len(names):
#     print(names[index])
#     #change the condition!!
#     index = index + 1

#----------------------------------------------------

# people = ['Mosiah', 'Andrade']

# for name in people:
#     print(name)

# index = 0
# while index < len(people):
#     print(people[index])
#     #change the condition!!
#     index = index + 1

#-------------------------------------------------

# This loop will start with 100, and go up to, but not including 200
#for i in range(100, 200):
#    print(i)

# This loop will do the same thing, but this time, it will count by 10's
#for i in range(100, 200, 10):
#    print(i)

#-----------------------------------

# color = ["red0", "blue", "green", "yellow"]

# for i in color:
#     print(i)

# for i in range(1,9):
#     print(i)

# for i in range(2,21,2):
#     print(i)
#-----------------------------------------

# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")