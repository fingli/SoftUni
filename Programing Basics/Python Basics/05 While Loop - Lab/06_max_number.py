import sys

max_number = -sys.maxsize

while True:
    initial = input()

    if initial == "Stop":
        break

    number = int(initial)

    if number > max_number:
        max_number = number

print(max_number)
