length = int(input())
width = int(input())

all_pieces = length * width

has_left = False

while all_pieces >= 0:
    piece_cake = input()

    if piece_cake == "STOP":
        has_left = True
        print(f"{all_pieces} pieces are left.")
        break

    all_pieces -= int(piece_cake)

if not has_left:
    print(f"No more cake left! You need {abs(all_pieces)} pieces more.")
