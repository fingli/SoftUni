price_vac = float(input())
puzzles = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
lorries = int(input())

sum_toys = (puzzles * 2.6) + (dolls * 3) + (teddies * 4.1) + (minions * 8.2) + (lorries * 2)
num_toys = puzzles + dolls + teddies + minions + lorries

if num_toys >= 50:
    sum_toys = sum_toys - (sum_toys * 0.25)

naem = sum_toys * 0.1
profit = sum_toys - naem
diff = abs(profit - price_vac)

if profit >= price_vac:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
