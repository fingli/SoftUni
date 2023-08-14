text_input = input()
summarum = 0

for char in text_input:
    if char == "a":
        summarum = summarum + 1
    elif char == "e":
        summarum = summarum + 2
    elif char == "i":
        summarum = summarum + 3
    elif char == "o":
        summarum = summarum + 4
    elif char == "u":
        summarum = summarum + 5

print(summarum)
