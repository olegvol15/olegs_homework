number = int(input("Enter a number from 3 to 9: "))

if 3 <= number <= 9:
    for i in range(1, number + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        for j in range(i - 1, 0, -1):
            line += str(j)
        print(line)
else:
    print("ERROR")
