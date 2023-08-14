price_cpu_usd = float(input())
price_vid_usd = float(input())
price_ram_usd = float(input())
number_ram = int(input())
percent_discount = float(input())

cpu_bgn = price_cpu_usd * 1.57
vid_bgn = price_vid_usd * 1.57
ram_bgn = price_ram_usd * 1.57

total_price_ram = number_ram * ram_bgn
total_price_cpu = cpu_bgn * (1 - percent_discount)
total_price_vid = vid_bgn * (1 - percent_discount)

total_price = total_price_cpu + total_price_vid + total_price_ram
print(f"Money needed - {total_price:.2f} leva.")
