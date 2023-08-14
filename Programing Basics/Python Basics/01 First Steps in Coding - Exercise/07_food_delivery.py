chicken = 10.35
fish = 12.4
vegetarian = 8.15

delivery = 2.5

num_chicken = int(input())
num_fish = int(input())
num_veg = int(input())

prise_chicken = num_chicken * chicken
prise_fish = num_fish * fish
prise_veg = num_veg * vegetarian

total = prise_chicken + prise_fish + prise_veg

desert = total * 0.2

whole = total + desert + delivery

print(whole)
