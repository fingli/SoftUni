first = int(input())
second = int(input())
operator = input()

result = 0
zero_flag = False

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    if second == 0:
        zero_flag = True
    else:
        result = first / second
elif operator == "%":
    if second == 0:
        zero_flag = True
    else:
        result = first % second

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        print(f"{first} {operator} {second} = {result} - even")
    else:
        print(f"{first} {operator} {second} = {result} - odd")

if operator == "/":
    if zero_flag:
        print(f"Cannot divide {first} by zero")
    else:
        print(f"{first} / {second} = {result:.2f}")
if operator == "%":
    if zero_flag:
        print(f"Cannot divide {first} by zero")
    else:
        print(f"{first} % {second} = {result}")
