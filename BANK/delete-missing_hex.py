import digits
import checksum
import wrong_checksum



def missing_piece_hex(integer):

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

    print(" --------------- " + str(number_in_digits))
    for i in range(9):
        x = number_in_digits[i]
        print(x)
        if x == 0:
            number_in_digits[i] = 1
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 2
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 0

        if x == 1:
            number_in_digits[i] = 0
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 2
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 1

        if x == 2:
            number_in_digits[i] = 0
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 1
            print(number_in_digits)
            if number_in_digits in digits.translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 2

    unique = []
    [unique.append(x) for x in possibilities if x not in unique]
    account = wrong_checksum.possible_outcomes(integer, unique)
    return account
    '''
    if len(unique) == 1:
        return unique
    elif len(unique) == 0:
        integer.append(" ILL")
        return integer
    else:
        possible_solutions = []
        for entry in unique:
            if checksum.checksum(entry) == True:
                possible_solutions.append(entry)
        if len()
        # several solutions possible - need checksum again
    '''

    