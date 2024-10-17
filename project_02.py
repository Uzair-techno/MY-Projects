# This program takes the item prices and
# calculates the total price including tax.

item_prices = [15, 20, 45, 14, 9]

total_price = sum(item_prices)
print(f"The total price is {total_price}$.")

tax = (total_price * 7) / 100
print(f"The total tax is {tax}$.")
total_price_include_tax = total_price + tax

print(f"You have to pay {total_price_include_tax}$.")