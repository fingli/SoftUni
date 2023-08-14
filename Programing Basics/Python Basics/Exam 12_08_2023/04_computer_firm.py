n_pc = int(input())

number_sales = 0
current_rating = 0

for every_n in range(n_pc):
    input_line = input()

    rating = input_line[2]
    possible_sales = int(input_line) // 10

    if int(rating) == 2:
        possible_sales = 0
    elif int(rating) == 3:
        possible_sales *= 0.5
    elif int(rating) == 4:
        possible_sales *= 0.7
    elif int(rating) == 5:
        possible_sales *= 0.85
    elif int(rating) == 6:
        possible_sales *= 1.00

    number_sales += possible_sales
    current_rating += int(rating)

average_rating = current_rating / n_pc

print(f"{number_sales:.2f}")
print(f"{average_rating:.2f}")
