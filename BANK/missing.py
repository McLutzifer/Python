from digits import *
import checksum
import wrong_checksum

def missing_piece(integer, account):     

    possibilities = []
    number_in_digits = []

    for i in range(3):          # 'translating' symbols into numbers like in digits.py
        for j in range(3):
            if integer[i][j] == " ":
                number_in_digits.append(0)
            if integer[i][j] == "|":
                number_in_digits.append(1)
            if integer[i][j] == "_":
                number_in_digits.append(2)
            if integer[i][j] == "\\":
                number_in_digits.append(3)
            if integer[i][j] == "/":
                number_in_digits.append(4)

    for i in range(9):                  # checks when one single symbol is replaced, if whole 3x3 represents a number 
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

    unique = [] 
    [unique.append(x) for x in possibilities if x not in unique]
    account = wrong_checksum.possible_outcomes(integer, unique)
    return account