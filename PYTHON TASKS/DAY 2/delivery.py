# Q7. Delivery Charge & Earnings

n = int(input("Number of Deliveries: "))

total_distance = 0
total_earnings = 0

for i in range(1, n + 1):

    distance = float(input(f"Distance for delivery {i}: "))

    total_distance += distance

    if distance <= 5:
        earning = 40
    else:
        earning = 40 + (distance - 5) * 8

    total_earnings += earning


average_distance = total_distance / n


print("\n----- DELIVERY EARNINGS REPORT -----")
print(f"Total Distance  : {total_distance:.2f} km")
print(f"Total Earnings  : ₹{total_earnings:.2f}")
print(f"Average Distance: {average_distance:.2f} km")