#def missing_piece(integer, account):     ##### MISSING PIECE STUFF  add account




possibilities = []

integer = ["   ","| |", "  |"]   #verwortackelter vierer
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

print(" --------------- " + str(number_in_digits))
for i in range(9):
    x = number_in_digits[i]
    print(x)
    if x == 0:
        number_in_digits[i] = 1
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 2
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 0

    if x == 1:
        number_in_digits[i] = 0
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 2
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 1

    if x == 2:
        number_in_digits[i] = 0
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 1
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        number_in_digits[i] = 2

unique = []
[unique.append(x) for x in possibilities if x not in unique]
account = possible_outcomes(integer, unique)


print(account)