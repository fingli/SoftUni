import math

days_absence = int(input())
food_left = int(input())
first_deer_per_day = float(input())
second_deer_per_day = float(input())
third_deer_per_day = float(input())

total_food_needed = (first_deer_per_day * days_absence) + (second_deer_per_day * days_absence) + (third_deer_per_day * days_absence)

if total_food_needed < food_left:
    diff = math.floor(food_left - total_food_needed)
    print(f"{diff} kilos of food left.")
elif total_food_needed > food_left:
    diff = math.ceil(total_food_needed - food_left)
    print(f"{diff} more kilos of food are needed.")
