days = int(input())
pom = input()
evaluation = input()

nights = days - 1
room_for_one = 18
apartment = 25
president_apartment = 35

if days < 10:
    if pom == "apartment":
        apartment = apartment - (apartment * 0.30)
    elif pom == "president apartment":
        president_apartment = president_apartment - (president_apartment * 0.10)
elif 10 <= days <= 15:
    if pom == "apartment":
        apartment = apartment - (apartment * 0.35)
    elif pom == "president apartment":
        president_apartment = president_apartment - (president_apartment * 0.15)
elif days > 15:
    if pom == "apartment":
        apartment = apartment - (apartment * 0.50)
    elif pom == "president apartment":
        president_apartment = president_apartment - (president_apartment * 0.20)

if evaluation == "positive":
    room_for_one = room_for_one + (room_for_one * 0.25)
    apartment = apartment + (apartment * 0.25)
    president_apartment = president_apartment + (president_apartment * 0.25)
elif evaluation == "negative":
    room_for_one = room_for_one - (room_for_one * 0.10)
    apartment = apartment - (apartment * 0.10)
    president_apartment = president_apartment - (president_apartment * 0.10)

if pom == "room for one person":
    print(f"{nights * room_for_one:.2f}")
elif pom == "apartment":
    print(f"{nights * apartment:.2f}")
elif pom == "president apartment":
    print(f"{nights * president_apartment:.2f}")
