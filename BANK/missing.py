import digits
import checksum
import wrong_checksum

def missing_piece(integer, account):     ##### MISSING PIECE STUFF  add account

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

    #print(" --------------- " + str(number_in_digits))

    for i in range(9):
        x = number_in_digits[i]

        for num in range(5):
            if x == num:
                for y in range(5):
                    if y != num:
                        x = y
                        if number_in_digits in translation:
                            possibilities.append(number_in_digits)
                            print("WWWWUUUUHUHHHHUHUHUHUHUHUHUHUHUH")
                    else:
                        continue
                x = num

    unique = []
    [unique.append(x) for x in possibilities if x not in unique]
    account = wrong_checksum.possible_outcomes(integer, unique)
    return account