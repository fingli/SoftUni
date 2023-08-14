deposit = float(input())
months = int(input())
yearly_interest = float(input())

cumulative_interest = deposit * (yearly_interest / 100)
monthly_interest = cumulative_interest / 12
# print(monthly_interest)
total_sum = deposit + (months * monthly_interest)

print(total_sum)
