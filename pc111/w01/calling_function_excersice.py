'''Problem Statement
In our modern world economy, many items are manufactured in large factories, 
then packed in boxes and shipped to distribution centers and retail stores. 
A common question for employees who pack items is “How many boxes do we need?”

Assignment
A manufacturing company needs a program that will help its employees pack 
manufactured items into boxes for shipping. Write a Python program named that 
asks the user for two integers:boxes.py

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the 
items. This must be a whole number. Note that the last box may be packed with 
fewer items than the other boxes.'''

import math

#keep the number of items
item = int(input('Enter the number of Items: '))

#keep the number of items per box
item_per_box = int(input('Enter the number of Items per Box: '))

#print the result resolving, deviding the number of items in items oer box to know how many box you will need
print(f'For {item} item, packing {item_per_box} items in each box, you will need {math.ceil(item / item_per_box)} boxes.')  #the formula is (x / y = z)