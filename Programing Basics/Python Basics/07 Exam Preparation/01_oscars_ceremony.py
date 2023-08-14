rent = int(input())

statues = rent - (rent * 0.3)
catering = statues - (statues * 0.15)
sound = catering / 2

spending = rent + statues + catering + sound

print(f"{spending:.2f}")
