price_m_sq = 7.61
discount = 18 / 100

sq_meters_greening = float(input())

price_calc = sq_meters_greening * price_m_sq
total_discount = price_calc * discount

total_price = price_calc - total_discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {total_discount} lv.')
