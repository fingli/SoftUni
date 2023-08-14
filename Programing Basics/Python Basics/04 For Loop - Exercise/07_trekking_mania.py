number_groups = int(input())

whole_sum_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest =0

for every_group in range(1, number_groups + 1):
    number_people = int(input())

    whole_sum_people += number_people

    if number_people <= 5:
        musala += number_people
    elif 6 <= number_people <= 12:
        montblanc += number_people
    elif 13 <= number_people <= 25:
        kilimanjaro += number_people
    elif 26 <= number_people <= 40:
        k2 += number_people
    elif number_people > 40:
        everest += number_people

print(f"{(musala / whole_sum_people) * 100:.2f}%")
print(f"{(montblanc / whole_sum_people) * 100:.2f}%")
print(f"{(kilimanjaro / whole_sum_people) * 100:.2f}%")
print(f"{(k2 / whole_sum_people) * 100:.2f}%")
print(f"{(everest / whole_sum_people) * 100:.2f}%")
