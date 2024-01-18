book_of_mormon = []

with open("w06/books.txt") as books:
    for book in books:
        #print(book.strip())

        book = book.strip()
        book_of_mormon.append(book)

print(book_of_mormon)

for book in book_of_mormon:
    print(book)

    