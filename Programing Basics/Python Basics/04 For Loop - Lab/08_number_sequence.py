import sys

numbers = int(input())
max_size = -sys.maxsize
min_size = sys.maxsize

for i in range(numbers):
    enter_numbers = int(input())
    if enter_numbers > max_size:
        max_size = enter_numbers
    if enter_numbers < min_size:
        min_size = enter_numbers

print(f"Max number: {max_size}")
print(f"Min number: {min_size}")
