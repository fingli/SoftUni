num_sea = int(input())
num_mountain = int(input())

profit = 0
flag_break = False

while True:
    name_package = input()

    if name_package == "Stop":
        break
    elif name_package == "sea":
        if num_sea <= 0:
            continue
        num_sea -= 1
        profit += 680

    elif name_package == "mountain":
        if num_mountain <= 0:
            continue
        num_mountain -= 1
        profit += 499

    if num_sea <= 0 and num_mountain <= 0:
        flag_break = True

    if flag_break:
        print(f"Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")
