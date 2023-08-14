city = input()
volume = float(input())

# if volume < 0:
#     print('error')

percent_sales = 0

if (volume > 0) and (city == 'Sofia' or city == 'Varna' or city == 'Plovdiv'):
    if 0 <= volume <= 500:
        if city == 'Sofia':
            percent_sales = 0.05
        elif city == 'Varna':
            percent_sales = 0.045
        elif city == 'Plovdiv':
            percent_sales = 0.055
    elif 500 <= volume <= 1000:
        if city == 'Sofia':
            percent_sales = 0.07
        elif city == 'Varna':
            percent_sales = 0.075
        elif city == 'Plovdiv':
            percent_sales = 0.08
    elif 1000 <= volume <= 10000:
        if city == 'Sofia':
            percent_sales = 0.08
        elif city == 'Varna':
            percent_sales = 0.1
        elif city == 'Plovdiv':
            percent_sales = 0.12
    elif volume > 1000:
        if city == 'Sofia':
            percent_sales = 0.12
        elif city == 'Varna':
            percent_sales = 0.13
        elif city == 'Plovdiv':
            percent_sales = 0.145
    trade_comm = volume * percent_sales
    print(f'{trade_comm:.2f}')

else: print('error')
