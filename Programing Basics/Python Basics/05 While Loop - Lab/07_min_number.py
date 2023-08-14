import sys

min_number = sys.maxsize

while True:
    initial = input()

    if initial == "Stop":
        break

    number = int(initial)

    if number < min_number:
        min_number = number

print(min_number)
