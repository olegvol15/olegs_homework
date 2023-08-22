# rows = int(input("Enter the amount of rows: "))
# for i in range(1, rows + 1):
#     line = "{:<{width}}".format(i, width=rows)
#     print(line)

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    if i == 1:
        line = "1"
    else:
        zeros = "0" * (i - 1)
        line = "1" + zeros
    print("{:>2} {:>20}".format(i, line))
