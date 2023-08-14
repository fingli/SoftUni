p_nylon = 1.5
p_dye = 14.5
p_solvent = 5
bags = 0.4

q_nylon = int(input())
q_dye = int(input())
q_solvent = int(input())
hours = int(input())

extra_nylon = 2
extra_dye = (q_dye * 0.1)

expense_nylon = (q_nylon + extra_nylon) * p_nylon
expense_dye = (q_dye + extra_dye) * p_dye
expense_solvent = q_solvent * p_solvent

sum_total = expense_nylon + expense_dye + expense_solvent + bags

work = (sum_total * 0.3) * hours

grand_total = sum_total + work

print(grand_total)
