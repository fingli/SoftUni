type_flowers = input()
number_flowers = int(input())
budget = int(input())

price = 0

if type_flowers == "Roses":
    price = 5
    if number_flowers > 80:
        price = price - (price * 0.10)
elif type_flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        price = price - (price * 0.15)
elif type_flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        price = price - (price * 0.15)
elif type_flowers == "Narcissus":
    price = 3
    if number_flowers < 120:
        price = price + (price * 0.15)
elif type_flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        price = price + (price * 0.20)

total = number_flowers * price

if total <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
