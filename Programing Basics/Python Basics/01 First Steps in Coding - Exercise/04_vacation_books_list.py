total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time_needed = total_pages // pages_per_hour

hours_per_day = total_time_needed // days

print(hours_per_day)
