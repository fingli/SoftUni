age = int(input())
washing_m = float(input())
toy = int(input())

money = 0
counter_m = 0
counter_t = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        counter_m += 1
        money = money + (counter_m * 10)
    else:
        counter_t += 1

toys_sold = counter_t * toy
brother = counter_m * 1

total_savings = (money + toys_sold) - brother

if total_savings >= washing_m:
    print(f"Yes! {total_savings - washing_m:.2f}")
else:
    print(f"No! {abs(total_savings - washing_m):.2f}")
