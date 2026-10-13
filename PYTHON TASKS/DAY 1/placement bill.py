items = []

while True:
    price = input("Enter item price (or 'done'): ")

    if price.lower() == "done":
        break

    try:
        price = float(price)

        if price < 0:
            print("Price cannot be negative.")
        else:
            items.append(price)

    except ValueError:
        print("Invalid price. Enter a number.")


subtotal = sum(items)

# Example discount slabs
if subtotal >= 1000:
    discount_rate = 0.10
elif subtotal >= 500:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate

# Example tax rate
tax_rate = 0.05
tax = (subtotal - discount) * tax_rate

final_amount = subtotal - discount + tax


print("\nItem         Price")
print("-------------------------")

for i, price in enumerate(items, start=1):
    print(f"Item {i:<5} {price:>8.2f}")

print("-------------------------")
print(f"Subtotal     {subtotal:>10.2f}")
print(f"Discount     {discount:>10.2f}")
print(f"Tax          {tax:>10.2f}")
print(f"Final        {final_amount:>10.2f}")