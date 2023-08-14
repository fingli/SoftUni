floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors + 1)):
    if floor % 2:
        room_type = "A"
    else:
        room_type = "O"

    if floor == floors:
        room_type = "L"

    for room in range(rooms):
        print(f"{room_type}{floor}{room}", end=" ")

    print()
