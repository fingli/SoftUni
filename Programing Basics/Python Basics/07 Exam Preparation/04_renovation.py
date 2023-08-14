import math

height = int(input())
width = int(input())
percent_not_painted = int(input())

whole_area = 4 * height * width
painted_area = math.ceil(whole_area - (whole_area * percent_not_painted / 100))

dye_liters = 0

while True:
    line_input = input()
    if line_input == "Tired!":
        print(f"{painted_area} quadratic m left.")
        break

    dye_liters = int(line_input)
    painted_area -= dye_liters

    if painted_area < 0:
        print(f"All walls are painted and you have {abs(painted_area)} l paint left!")
        break
    elif painted_area == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
