import math

w_record = float(input())
length = float(input())
time_1_m = float(input())

total_length_time = length * time_1_m
add_delay = math.floor(length / 15) * 12.5

total_time = total_length_time + add_delay

if total_time >= w_record:
    diff = total_time - w_record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
