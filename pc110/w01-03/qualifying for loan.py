"""
Author: Mosiah Andrade

Purpose: Practice if statements with loan questions
"""


loan_large = int(input('In a rating from 1-10 \n \nhow large is the loan? '))
credit_history = int(input('How good is your cradit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

decision = False

if loan_large >= 5:
    if credit_history >= 7 and income >= 7:
        decision = True
    elif (credit_history >= 7 or income >= 7) and down_payment >= 5:
        decision = True
    else:
        decision = False

else:
    if credit_history < 4:
        decision = False
    elif income >= 7 or down_payment >= 7:
        decision = True
    elif income >= 4 and down_payment >= 4:
        decision = True
    else:
        decision = False

if decision:
    print('') #print blank space
    print('Congratulation, our decision is, Yes!')
else:
    print('Sorry, our decision is, no.')