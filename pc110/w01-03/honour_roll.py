gpa = float(input("What was your grade point average? "))
lowest_grade = float(input("What was your lowest grade? "))

if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else: 
	honour_roll = False

if honour_roll: #it's mean that if honour_roll is true, execute
	print('Well done!')