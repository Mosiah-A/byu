# # courses_file = open("w06\courses.txt")

# with open("w06/courses.txt") as courses_file:
#     for line in courses_file:
#         if "CSE 110" in line:
            
#             print(f"{line} - introduce to programming")
#         else:
#             print(line)

#     print("good bye")

# print("It's cloused now")
# courses_file.close()

''' 
spliting strings
'''
# # colors = "red green blue yellow"

# colors = "red,green,blue,yellow"

# # colors_part = colors.split() #transform in a list
# colors_part = colors.split(",") #split in , places

# print(colors)
# print(colors_part)

#Removing whitespace from strings

# name = "   Mosiah Andrade         "



# clean_name = name.strip()

# print(f'---------{name}----------')


# print(f'---------{clean_name}----------')

with open("w06\courses.txt") as courses_file:
    for line in courses_file:

        #line.strip()#to delet extra line

        parts = line.split(",")

        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus: {bonus_grade}")