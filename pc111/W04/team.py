import random 

def main():
    number = [16.2, 75.1, 52.3]
    print(number)
    print()
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    print()
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")
    print()

def append_random_numbers(numbers_list, quantity):
    for _ in range(quantity):
        number = random.uniform(0, 100)
        rounded = round(number)
        numbers_list.append(round)

if __name__ == '__main__':
    main()


