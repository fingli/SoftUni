budget = float(input())
num_nights = int(input())
price_night = float(input())
percent_additional = int(input())

if num_nights > 7:
    price_night = price_night - (price_night * 0.05)

sum_nights = num_nights * price_night
sum_additional = budget * percent_additional / 100

total_sum_needed = sum_nights + sum_additional

if total_sum_needed <= budget:
    diff = budget - total_sum_needed
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    diff = total_sum_needed - budget
    print(f"{diff:.2f} leva needed.")
