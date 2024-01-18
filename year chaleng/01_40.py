'''
This Python code interacts with the user through inputs to perform various string 
manipulation operations. Initially, it prompts for two strings, concatenates them, 
and prints the result. Next, it reverses a given word, displaying its characters in 
reverse order. Subsequently, it counts and prints the number of vowels (considering 
both uppercase and lowercase) in a word provided by the user. Finally, it substitutes 
one specific letter for another in a given word, displaying the resulting string. Each 
section of the code highlights different aspects of string manipulation in Python, 
offering diverse practice for the involved concepts.
'''

t1 = input('Enter the first string: ')
t2 = input('Enter the second string: ')

print(t1, t2, sep=" ")

word = input('Enter a word: ')
lenword = int(len(word))


while lenword >= 1:
    print(f"{word[lenword-1]}",end="")
    lenword = lenword - 1


cword = input('Enter a word: ')
cword = cword.upper()
lenword = len(cword)
count = 0

while lenword >= 1:
    if cword[lenword-1] == 'A' or cword[lenword-1] == "E" or cword[lenword-1] == 'I' or cword[lenword-1] == "O" or cword[lenword-1] == 'U':
        count = count + 1
    lenword = lenword - 1

print(count)


sword = input('Enter a word: ')
fl = input("Enter the letter to find: ")
cl = input("Enter the letter to change: ")

lenword = len(sword)

ns = ""
for c in sword:
    if c == fl:
        ns += cl
    else:
        ns += c
print(ns)