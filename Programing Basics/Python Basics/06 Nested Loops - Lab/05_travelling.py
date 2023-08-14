flag_break = False

while True:
    destination = input()

    if destination == "End":
        flag_break = True
        break

    budget = float(input())
    savings = 0


    while savings < budget:
        enter_savings = input()

        if enter_savings == "End":
            flag_break = True
            break

        else:
            savings += float(enter_savings)

    if not flag_break:
        print(f"Going to {destination}!")

    else:
        break
