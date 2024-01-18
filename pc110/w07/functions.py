# from datetime import datetime

# def print_time():
# 	print('task completed')
# 	print(datetime.now())
# 	print()

# first_name = 'Susan'
# print_time()

# for x in range (0,10):
# 	print(x)
# print_time()

from datetime import datetime

def print_time(task_name):
	print(task_name)
	print(datetime.now())
	print()

first_name = 'Susan'
print_time('first name assigned')

for x in range (0,10):
	print(x)
print_time('loop completed')

#---------------------------------------------------

def get_initial(name):
	initial = name[0:1].upper()
	return initial

first_name = input('Enter your firstname: ')
fisrt_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get-initial(last_name)