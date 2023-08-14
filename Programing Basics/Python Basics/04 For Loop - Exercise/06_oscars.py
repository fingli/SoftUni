name = input()
points_academy = float(input())
number_eval = int(input())

points_actor = points_academy

for every_eval in range(1, number_eval + 1):
    name_eval = input()
    points_eval = float(input())
    points_actor +=  ((len(name_eval) * points_eval) / 2)

    if points_actor > 1250.5:
        break

if points_actor < 1250.5:
    print(f"Sorry, {name} you need {1250.5 - points_actor:.1f} more!")
else:
    print(f"Congratulations, {name} got a nominee for leading role with {points_actor:.1f}!")
