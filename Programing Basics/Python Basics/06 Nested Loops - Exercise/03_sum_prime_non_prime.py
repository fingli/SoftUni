input_line = input()

sum_prime = 0
sum_non_prime = 0

while input_line != "stop":
    current_num = int(input_line)

    if current_num < 0:
        print("Number is negative.")
        input_line = input()
        continue

    counter = 0
    for every_i in range (1, current_num + 1):
        if current_num % every_i == 0:
            counter +=1

    if counter == 2:
        sum_prime += current_num
    else:
        sum_non_prime += current_num

    input_line = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
