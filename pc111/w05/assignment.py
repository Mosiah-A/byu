def main():
    text_list = read_list('provinces.txt')
    

def read_list(filename):
    provinces_list = []

    with open('provinces.txt', 'rt') as text_file:
        
        for line in text_file:
            clean_line = line.strip()

            provinces_list.append(clean_line)
        print(provinces_list)
    

if __name__ ==  '__main__':
    main()