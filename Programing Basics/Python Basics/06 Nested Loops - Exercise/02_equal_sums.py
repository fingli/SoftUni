first_n = int(input())
second_n = int(input())

for number in range(first_n, second_n + 1):
    num_to_str = str(number)

    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=" ")
