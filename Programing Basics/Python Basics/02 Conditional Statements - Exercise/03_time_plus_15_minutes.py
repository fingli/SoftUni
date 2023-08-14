hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
total_minutes = minutes + hours_to_minutes

add_fifteen = total_minutes + 15

hours_new = add_fifteen // 60
minutes_new = add_fifteen % 60

if hours_new == 24:
    hours_new = 0

if minutes_new < 10:
    print(f"{hours_new}:0{minutes_new}")
else:
    print(f"{hours_new}:{minutes_new}")
