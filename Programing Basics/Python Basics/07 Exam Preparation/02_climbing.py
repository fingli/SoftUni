record = float(input())
length = float(input())
time = float(input())

tilt = (length // 50) * 30

total_time = (length * time) + tilt

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")
