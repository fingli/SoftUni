start_num = int(input())
end_num = int(input())
magic_num = int(input())

combination_counter = 0
flag_break = False

for every_i in range(start_num, end_num + 1):
    for every_j in range(start_num, end_num + 1):
        sum_comb = every_i + every_j
        combination_counter += 1

        if sum_comb == magic_num:
            print(f"Combination N:{combination_counter} ({every_i} + {every_j} = {magic_num})")
            flag_break = True
            break

    if flag_break:
        break

if not flag_break:
    print(f"{combination_counter} combinations - neither equals {magic_num}")


