from datetime import datetime

#function to print current date and time
def print_time():
    print('Task completed')
    print(datetime.now())
    print()

#print timestamps to see how long sections of code
#take to run

first_name = "Mosiah"
print_time()

for x in range (0,10):
    print(x)
print_time()


#customized message

def print_time(task_name):
    print(task_name)
    print('Task completed')
    print(datetime.now())
    print()

#print timestamps to see how long sections of code
#take to run

first_name = "Mosiah"
print_time('printed first name')

for x in range (0,10):
    print(x,end=', ')
print()
print_time('\ncompleted for loop')

#None function
#ask for someones name and return the initials
first_name = 'Mosiah'
first_name_initial = first_name[0:1]

middle_name = "Assunção"
middle_name_initial = middle_name[0:1]

last_name = "Andrade"
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial \
    + middle_name_initial + last_name_initial)

#with function and a return
def get_initial(name):
    initial = name [0:1].upper()
    return initial

first_name = 'Mosiah'
first_name_initial = get_initial(first_name)

middle_name = "Assunção"
middle_name_initial = get_initial(middle_name)

last_name = "Andrade"
last_name_initial = get_initial(last_name)


print('Your initials are: ' + first_name_initial \
    + middle_name_initial + last_name_initial)

#multiples parameter
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = 'mosiah'
first_name_initial = get_initial(first_name, False)#don't force upper case

print('Your initial is: ' + first_name_initial)

#specify a default value for a parameter

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = 'mosiah'
first_name_initial = get_initial(first_name)
print('Your initial is: ' + first_name_initial)

#You can namee=d when you call the function
first_name_initial = get_initial(name=first_name, force_uppercase=True)
print('Your initial is: ' + first_name_initial)
