budget = float(input())
vid = int(input())
cpu = int(input())
ram = int(input())

sum_vid = vid * 250
sum_cpu = cpu * sum_vid * 0.35
sum_ram = ram * sum_vid * 0.1

total = sum_vid + sum_cpu + sum_ram

if vid > cpu:
    total = total - (total * 0.15)

if budget >= total:
    leftover = budget - total
    print(f"You have {leftover:.2f} leva left!")
else:
    leftover = total - budget
    print(f"Not enough money! You need {leftover:.2f} leva more!")
