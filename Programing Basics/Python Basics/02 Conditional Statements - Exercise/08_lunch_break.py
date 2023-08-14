import math

name = str(input())
dur_tv = int(input())
dur_break = int(input())

spare_time = dur_break - (dur_break * 1/8) - (dur_break * 1/4)

if spare_time >= dur_tv:
    diff = math.ceil(spare_time - dur_tv)
    print(f"You have enough time to watch {name} and left with {diff} minutes free time.")
else:
    diff = math.ceil(dur_tv - spare_time)
    print(f"You don't have enough time to watch {name}, you need {diff} more minutes.")
