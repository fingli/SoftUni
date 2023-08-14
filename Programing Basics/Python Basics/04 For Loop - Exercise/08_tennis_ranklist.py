num_tours = int(input())
entry_points = int(input())

whole_points = 0
win_w = 0

for each_tour in range(1, num_tours + 1):
    stage = input()
    if stage == "W":
        whole_points += 2000
        win_w += 1
    elif stage == "F":
        whole_points += 1200
    elif stage == "SF":
        whole_points += 720

print(f"Final points: {whole_points + entry_points}")
print(f"Average points: {whole_points // num_tours}")
print(f"{win_w / num_tours * 100:.2f}%")
