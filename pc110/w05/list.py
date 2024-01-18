
# clients = []

# clients = ['Emilly', 'John', 'Mary']
# clients = list('1')
# print(clients)

friends = []
friends_name = ""


while friends_name != 'end':
    friends_name = input("Type the name of a friend: ")
    if friends_name != 'end':
        friends.append(friends_name.capitalize())
print('Your friends are:')
for friend in friends:
    print(friend, end=", ")