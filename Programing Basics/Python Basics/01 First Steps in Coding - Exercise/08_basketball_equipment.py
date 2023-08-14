year_tax = int(input())

kets = year_tax - (year_tax * 0.4)
ekip = kets - (kets * 0.2)
ball = ekip / 4
akses = ball / 5

total = year_tax + kets + ekip + ball + akses

print(total)
