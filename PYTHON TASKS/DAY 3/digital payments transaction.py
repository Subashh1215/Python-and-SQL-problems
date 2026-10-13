# Q7. Digital Payment Transaction Analyzer

n = int(input("Transactions: "))

successful = []
rejected = 0

for i in range(n):

    value = input()

    try:
        amount = float(value)

        if amount < 0:
            rejected += 1
        else:
            successful.append(amount)

    except ValueError:
        rejected += 1


if len(successful) > 0:

    total = sum(successful)
    highest = max(successful)
    lowest = min(successful)
    average = total / len(successful)

    print("Successful Transactions :", len(successful))
    print(f"Total Amount : ₹{total:.2f}")
    print(f"Highest Transaction : ₹{highest:.2f}")
    print(f"Lowest Transaction : ₹{lowest:.2f}")
    print(f"Average Transaction : ₹{average:.2f}")
    print("Rejected Transactions :", rejected)

else:

    print("Successful Transactions : 0")
    print("Total Amount : ₹0.00")
    print("No successful transactions.")
    print("Rejected Transactions :", rejected)