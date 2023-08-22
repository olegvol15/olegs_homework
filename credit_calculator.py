credit = float(input("Enter the sum of credit: "))
print("\nPayments for 1 year:")
remaining_credit = credit
default_percent = 0.02
print("{:<10} {:<20} {:<5}".format("Month", "Amount of payment", "Percent"))
print("=" * 45)
for month in range(1, 13):
    percent = default_percent * remaining_credit
    total = remaining_credit + percent
    print("{:<10} {:<20.2f} {:<15.2f}".format(month, total, percent))
    remaining_credit -= credit/12

print("\nPayments for 5 years:")
remaining_credit = credit
default_percent = 0.02
print("{:<10} {:<20} {:<15}".format("Month", "Amount of payment", "Percent"))
print("=" * 45)
for year in range(1, 6):
    for month in range(1, 13):
        percent = default_percent * remaining_credit
        total = remaining_credit + percent
        print("{:<10} {:<20.2f} {:<15.2f}".format((year - 1) * 12 + month, total, percent))
        remaining_credit -= credit/(5 * 12)
    if year <= 2:
        default_percent = 0.04
