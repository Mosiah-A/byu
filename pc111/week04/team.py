import random 

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    print()
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    print()
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")
    print()

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        number = random.uniform(0, 100)
        rounded = round(number)
        numbers_list.append(rounded)

if __name__ == '__main__':
    main()


