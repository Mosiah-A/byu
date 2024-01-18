# Author: Mosiah Andrade

# purpose: calculate areas od shapes
import math

# #area of a square
ls = input('What is the length of a side of the square? ')
print(f'The area of the square is: {float(ls)*float(ls)}')

#area of rectangle
lr = input('What is the length of a side of the Rectangle? ')
wr = input('what is the width of the rectangle? ')
print(f'The area of the square is: {float(wr)*float(lr)}')

#area of th circle
r = input('What is the radius of the circle? ')
pi = math.pi
ar = pi * float(r) ** 2
print(f'The area of the circle is: {ar:.1f}')
