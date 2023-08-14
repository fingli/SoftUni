name = input()
class_counter = 0
eval_points_sum = 0
exclude = 0

while True:
    eval_points = float(input())

    if eval_points < 4:
        exclude += 1

        if exclude > 1:
            print(f"{name} has been excluded at {class_counter + 1} grade")
            break

        continue

    else:
        eval_points_sum += eval_points
        class_counter += 1

    if class_counter == 12:
        average_eval = eval_points_sum / 12
        print(f"{name} graduated. Average grade: {average_eval:.2f}")
        break
