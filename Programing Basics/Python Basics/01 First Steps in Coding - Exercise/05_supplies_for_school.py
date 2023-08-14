price_pens = 5.8
price_markers = 7.2
price_deterg = 1.2

number_pens = int(input())
number_markers = int(input())
lt_deterg = int(input())
discount = int(input())

sum_pens = number_pens * price_pens
sum_markers = number_markers * price_markers
sum_deterg = lt_deterg * price_deterg

total_sum = sum_pens + sum_markers + sum_deterg
percent_disc = discount / 100

discounted_price = total_sum - (total_sum * percent_disc)

print(discounted_price)
