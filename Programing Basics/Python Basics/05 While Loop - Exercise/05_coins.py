change = float(input())
cents = change * 100

count = 0

while cents != 0:
    if cents >= 200:
        cents -= 200
    elif cents >= 100:
        cents -= 100
    elif cents >= 50:
        cents -= 50
    elif cents >= 20:
        cents -= 20
    elif cents >= 10:
        cents -= 10
    elif cents >= 5:
        cents -= 5
    elif cents >= 2:
        cents -= 2
    elif cents >= 1:
        cents -= 1
    else:
        break

    count += 1

print(count)
