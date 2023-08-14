budget = float(input())
season = input()

destination = ""
rest = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget = budget * 0.30
        rest = "Camp"
    elif season == "winter":
        budget = budget * 0.70
        rest = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget = budget * 0.40
        rest = "Camp"
    elif season == "winter":
        budget = budget * 0.80
        rest = "Hotel"
elif budget > 1000:
    destination = "Europe"
    budget = budget * 0.90
    rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{rest} - {budget:.2f}")
