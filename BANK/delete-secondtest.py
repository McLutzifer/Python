integer = [    "   ",    "| |",     "  |" ]


possibilities = []
number_in_digits = []

for i in range(3):
    for j in range(3):
        if integer[i][j] == " ":
            number_in_digits.append(0)
        if integer[i][j] == "|":
            number_in_digits.append(1)
        if integer[i][j] == "_":
            number_in_digits.append(2)
        ###############################
        ############ HEX ##############
        if integer[i][j] == "\\":
            number_in_digits.append(3)
        if integer[i][j] == "/":
            number_in_digits.append(4)






for i in range(9):
    x = number_in_digits[i]

    for num in range(5):
        if x == num:
            for y in range(5):
                if y != num:
                    x = y
                    if number_in_digits in translation:
                        possibilities.append(number_in_digits)
                else:
                    continue
            x = num

    #if x == [num for num in range(5)]:
        #print(x)

    if x == 0:
        x = 1
        print("do stuff 1")
        x = 2
        print("do stuf 2")
        x = 0