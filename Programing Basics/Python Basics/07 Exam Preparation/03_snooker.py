stage = input()
ticket_type = input()
num_tickets = int(input())
photo = input()

price = 0
photo_price = 0

if photo == "Y":
    photo_price = 40

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

sum_tickets = num_tickets * price

if sum_tickets > 4000:
    sum_tickets = sum_tickets - (sum_tickets * 0.25)
    photo_price = 0
elif sum_tickets > 2500:
    sum_tickets = sum_tickets - (sum_tickets * 0.10)

total = sum_tickets + (photo_price * num_tickets)
print(f"{total:.2f}")
