account = 0

while True:
    data = input()

    if data == "NoMoreMoney":
        break

    payment = float(data)

    if payment >= 0:
        account += payment
        print(f"Increase: {payment:.2f}")

    else:
    #if account < 0:
        print("Invalid operation!")
        break

print(f"Total: {account:.2f}")
