principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))

if principal < 0 or time < 0:
    print("Invalid input. Principal and time must be non-negative.")
else:
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print(f"\nPrincipal       : {principal:.2f}")
    print(f"Rate            : {rate:.2f}%")
    print(f"Time            : {time:.2f} years")
    print(f"Simple Interest : {simple_interest:.2f}")
    print(f"Total Amount    : {total_amount:.2f}")