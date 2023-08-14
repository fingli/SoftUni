import math

num_people = int(input())
entrance = float(input())
price_chezlong = float(input())
price_umbrella = float(input())

sum_expence = num_people * entrance
wanting_shezlong = math.ceil(num_people * 0.75)
number_umbrellas = math.ceil(num_people / 2)

expence_shezlong = wanting_shezlong * price_chezlong
expence_umbrellas = number_umbrellas * price_umbrella

total_sum = sum_expence + expence_shezlong + expence_umbrellas

print(f"{total_sum:.2f} lv.")
