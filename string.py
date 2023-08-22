line = input("Enter the line that has more than 15 symbols: ")
if len(line) < 16:
    print("Line is too short!")
else:
    char3 = line[3]
    print("Third char is ", char3)

    penultimate = line[-2]
    print("Penultimate char is ", penultimate)

    five_chars = line[:5]
    print("First five chars are: ", five_chars)

    allbutTwo = line[:-2]
    print("All except last two: ", allbutTwo)

    evenIndex = line[::2]
    print("Even index chars: ", evenIndex)

    oddIndex = line[1::2]
    print("Odd index chars: ", oddIndex)

    reverse = line[::-1]
    print("Reversed string: ", reverse)

    reverseThroughOne = line[-1::-2]
    print("Reversed through one: ", reverseThroughOne)

    length = len(line)
    print("Length of the line is: ", length)
