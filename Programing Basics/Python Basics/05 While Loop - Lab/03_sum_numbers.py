i_number = int(input())

number_input = 0
sum_input = 0

while True:
    number_input = int(input())
    sum_input += number_input

    if sum_input >= i_number:
        break

print(sum_input)
