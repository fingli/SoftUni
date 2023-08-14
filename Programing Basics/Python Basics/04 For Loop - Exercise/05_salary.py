n_tabs = int(input())
salary = int(input())

# facebook = 150
# instagram = 100
# reddit = 50

for i in range(1, n_tabs + 1):
    tab = input()
    if tab == "Facebook":
        salary -= 150
        if salary <= 0:
            break
    elif tab == "Instagram":
        salary -= 100
        if salary <= 0:
            break
    elif tab == "Reddit":
        salary -= 50
        if salary <= 0:
            break
    else:
        continue

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)
