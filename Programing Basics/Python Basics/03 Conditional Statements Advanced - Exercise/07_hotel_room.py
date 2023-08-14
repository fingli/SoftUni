months = input()
num_nights = int(input())

app = 0
studio = 0

if months == "May" or months == "October":
    if 7 < num_nights <= 14:
        studio = 50 - (50 * 0.05)
    elif num_nights > 14:
        studio = 50 - (50 * 0.30)
    else:
        studio = 50
    app = 65
elif months == "June" or months == "September":
    if num_nights > 14:
        studio = 75.20 - (75.20 * 0.20)
    else:
        studio = 75.20
    app = 68.70
elif months == "July" or months == "August":
    studio = 76
    app = 77

if num_nights > 14:
    app = app - (app * 0.10)

print(f"Apartment: {num_nights * app:.2f} lv.")
print(f"Studio: {num_nights * studio:.2f} lv.")
