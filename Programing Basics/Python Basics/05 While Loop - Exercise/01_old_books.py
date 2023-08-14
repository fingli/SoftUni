book = input()

book_count = 0
found = False

current_book = input()
while current_book != "No More Books":

    if current_book == book:
        found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    current_book = input()

if not found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
