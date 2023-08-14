first_max_value = int(input())
second_max_value = int(input())
third_max_value = int(input())

for num1 in range(1, first_max_value + 1):
    for num2 in range(1, second_max_value + 1):
        counter = 0
        for every_i in range(1, num2 + 1):
            if num2 % every_i == 0:
                counter += 1
        for num3 in range(1, third_max_value + 1):
            if num1 % 2 == 0 and counter == 2 and num3 % 2 == 0:
                print(f"{num1} {num2} {num3}")
