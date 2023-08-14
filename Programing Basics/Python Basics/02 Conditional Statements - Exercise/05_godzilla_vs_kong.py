budget = float(input())
num_stunts = int(input())
price_outfit_1 = float(input())

decor = budget * 0.1
total_outfit = price_outfit_1 * num_stunts

if num_stunts > 150:
    total_outfit = total_outfit - (total_outfit * 0.1)

total_sum_movie = decor + total_outfit
diff = abs(total_sum_movie - budget)

if total_sum_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
