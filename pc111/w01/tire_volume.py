from datetime import datetime
import math

dt = datetime.now(tz=None)

w = int(input('Enter the width of the tire in mm (ex 205): ')) 
a = int(input('Enter the aspect radio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches(ex 15): '))
pi = math.pi


v = pi * w**2 * a * (w * a + 2540 * d) / 10000000000


print(70*'-')
print(f"The approcimate volume is {v:.2f} liters")
print(70*'-')


want_buy = input(f'Do you want buy tires with the {d} in:[Y/N] ')

if want_buy.upper() == 'Y':
    name = input("Enter your name: ")
    phone_number = input('Enter your phone number: ')
elif want_buy.upper() == 'N':
    name = None
    phone_number = None

print(70*'-')
print('')
print('''
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⠶⢶⡶⠶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⠀⡸⢇⠀⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⢏⡉⠻⢿⣿⣿⣿⠤⠧⠼⠤⣿⣿⣿⣿⠟⢩⠿⣦⠀⠀⠀
⠀⢀⣾⣅⠘⢡⠆⡴⠛⢉⣠⣤⣶⠀⠀⠀⠉⠛⢯⣠⠔⠠⠚⣷⡀⠀
⠀⣾⣿⣿⣷⣦⡞⢀⣴⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢻⣤⣶⣿⣿⣷⠀
⢠⣿⣿⣿⣿⡟⠀⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⡇⠘⠛⠛⠛⠛⠛⠛⣤⣤⣤⣤⣤⣤⡄⢸⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⠀⣼⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠟⠁⣼⣿⣿⣿⣿⡿⠀
⠀⠈⢿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠿⠛⠋⣁⣤⣾⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
''')
print('           Thanks \n       Program closed')
print('')
print(70*'-')




with open("volume.txt", mode="at") as volume_file:
    print(f"{dt: %Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {name}, {phone_number} ", file=volume_file)
