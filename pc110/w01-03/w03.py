# province = input("What province do you live? ")
# tax = 0

# if provice == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

province = input("What province do you live? ")
tax = 0

# if provice == 'Alberta' or province == 'Nunavut':
#     tax = 0.05
if provice.lower in('alberta' , 'aunavut' , 'aukon'):
    tax = 0.05
elif province.lower == 'ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)