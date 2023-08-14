length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
convert_lt = volume / 1000
dec_percent = percent / 100

liters = convert_lt * (1 - dec_percent)

print(liters)
