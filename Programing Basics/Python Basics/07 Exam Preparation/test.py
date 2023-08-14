first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    num_to_str = str(number)
    counter = 0

    for index, digit in enumerate(num_to_str, start=1):
        if int(digit) % 2 == 0:
            continue

        counter += int(index)

        if counter == 10:
            print(num_to_str, end=" ")
