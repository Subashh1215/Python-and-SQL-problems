# Q4. Formatted Electricity Bill

customer = input("Enter customer name: ")
units = float(input("Enter units consumed: "))

bill = 0

# Example slab structure
if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)

elif units <= 300:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 4)

else:
    bill = (100 * 2) + (100 * 3) + (100 * 4) + ((units - 300) * 5)


print("\n----- ELECTRICITY BILL -----")
print(f"Customer : {customer}")
print(f"Units    : {units:.0f}")
print(f"Amount   : ₹{bill:.2f}")