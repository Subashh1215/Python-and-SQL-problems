# Q6. Digital Parking Fee

entry = input("Entry Time: ")
exit_time = input("Exit Time: ")


# Convert entry time into minutes

entry_hour = int(entry[0:2])
entry_minute = int(entry[3:5])

entry_total = entry_hour * 60 + entry_minute


# Convert exit time into minutes

exit_hour = int(exit_time[0:2])
exit_minute = int(exit_time[3:5])

exit_total = exit_hour * 60 + exit_minute


# Handle midnight crossing

if exit_total < entry_total:
    exit_total = exit_total + 24 * 60


# Calculate duration

duration = exit_total - entry_total

hours = duration // 60
minutes = duration % 60


# Calculate billable hours
# Any part of an hour counts as a full hour

billable_hours = (duration + 59) // 60


# Calculate fee

if billable_hours <= 1:
    fee = 30
else:
    fee = 30 + (billable_hours - 1) * 20


print("\n----- PARKING RECEIPT -----")
print(f"Parking Duration : {hours} hours {minutes} minutes")
print(f"Billable Hours   : {billable_hours}")
print(f"Parking Fee      : ₹{fee}")