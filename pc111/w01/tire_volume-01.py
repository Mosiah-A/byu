# v= pi * w**2 * a *(w*a +2,540*d)
# 

import math


w = int(input('Enter the width of the tire in mm (ex 205): ')) 
a = int(input('Enter the aspect radio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches(ex 15): '))
pi = math.pi


v = pi * w**2 * a * (w * a + 2540 * d) / 10000000000

print(f"The approcimate volume is {v:.2f} liters")
