import random

def main():
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        reverse = reverse_list(fruit_list)
        print(f'reversed: {reverse}')
        fruit_list.append('orange')
        print(f'append orange: {fruit_list}')
        insert_cherry(fruit_list)
        print(f'insert cherry: {fruit_list}')
        remove_banana = fruit_list.remove('banana')
        print(f'removed banana: {fruit_list}')
        pop_orange(fruit_list)
        print(f'pop orange: {fruit_list}')
        list_sorted = sorted_list(fruit_list)
        print(f'sorted: {list_sorted}')
        fruit_list.clear()
        print(f'cleared: {fruit_list}')
        
        
        

def reverse_list(original):
    index = len(original)
    reverse = []
    while index > 0:
        index -= 1
        reverse.append(original[index])
    return reverse

def insert_cherry(original):
    length = len(original)
    for index in range(length):
        if original[index] == 'apple':
            original.insert(index, 'cherry')
            break

def pop_orange(original):
    length = len(original)
    index = length - 1
    while index >= 0:
        if original[index] == 'banana':
            original.pop(index)
        index -= 1

def sorted_list(original):
    length = len(original)
    index = length - 1
    sorteds = []
    while index >= 0:
        sorted_item = random.choice(original)
        sorteds.append(sorted_item)
        index -= 1
    return sorteds
    

if __name__ == '__main__':
    main()