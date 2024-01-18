'''
Author: Mosiah Andrade

Purpose: List and analyse numbers
'''
#Variables block
numbers= []
new_number = None
total_sum = 0

#Headline
print("Enter a list of numbers, type 0 when finished")

#creating the list with user input
while new_number != 0:
    new_number = int(input("Enter number: "))
    numbers.append(new_number)

#summing the numbers
for number in numbers:
    total_sum +=  number

print(f"The sum is: {total_sum}")

#calculating the average
len_numbers = len(numbers) -1 #finding lenght by our list - 1 because was nullifying "zero" number
average = total_sum / len_numbers 

print(f"The average is: {average}")

#finding the largest number
largest = -1
for numeber in numbers:
    if number > largest:
        largest = number

print(f"The largest number is: {largest}")

smallest = 9999999999

for number in numbers:
    if number > 0 and number < smallest:
        smallest = number

print(f"The smallest positive number is: {smallest}")

sorted_list = sorted(numbers)

print("The sorted list is:")
for number in sorted_list:
    print(number)