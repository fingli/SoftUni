weight_parcel = float(input())
service = input()
distance = int(input())

price_per_km_leva = 0

if service == "standard":
    if weight_parcel < 1:
        price_per_km_leva = 0.03
    elif 1 <= weight_parcel < 10:
        price_per_km_leva = 0.05
    elif 10 <= weight_parcel < 40:
        price_per_km_leva = 0.10
    elif 40 <= weight_parcel < 90:
        price_per_km_leva = 0.15
    elif 90 <= weight_parcel < 150:
        price_per_km_leva = 0.20

if service == "express":
    if weight_parcel < 1:
        price_per_km_leva = 0.03 + (0.03 * weight_parcel * 0.80)
    elif 1 <= weight_parcel < 10:
        price_per_km_leva = 0.05 + (0.05 * weight_parcel * 0.40)
    elif 10 <= weight_parcel < 40:
        price_per_km_leva = 0.10 + (0.10 * weight_parcel * 0.05)
    elif 40 <= weight_parcel < 90:
        price_per_km_leva = 0.15 + (0.15 * weight_parcel * 0.02)
    elif 90 <= weight_parcel < 150:
        price_per_km_leva = 0.20 + (0.20 * weight_parcel * 0.01)

total_cost = distance * price_per_km_leva

print(f"The delivery of your shipment with weight of {weight_parcel:.3f} kg. would cost {total_cost:.2f} lv.")
