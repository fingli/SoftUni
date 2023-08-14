steps_sum = 0

while True:
    steps = input()

    if steps != "Going home":
        steps_sum += int(steps)
    else:
        home_steps = int(input())
        steps_sum += home_steps

        if steps_sum >= 10000:
            print(f"Goal reached! Good job!")
            print(f"{steps_sum - 10000} steps over the goal!")
            break
        else:
            print(f"{10000 - steps_sum} more steps to reach goal.")
            break

    if steps_sum >= 10000:
        print(f"Goal reached! Good job!")
        print(f"{steps_sum - 10000} steps over the goal!")
        break
