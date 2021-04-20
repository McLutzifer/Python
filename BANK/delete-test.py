
import sys


##################################
#             DIGITS         #
##################################
one = [
    "   ",
    "  |",
    "  |"
]

two = [
    " _ ",
    " _|",
    "|_ "
]

three = [
    " _ ",
    " _|",
    " _|"
]

four = [
    "   ",
    "|_|",
    "  |"
]

five = [
    " _ ",
    "|_ ",
    " _|"
]

six = [
    " _ ",
    "|_ ",
    "|_|"
]

seven = [
    " _ ",
    "  |",
    "  |"
]

eight = [
    " _ ",
    "|_|",
    "|_|"
]

nine = [
    " _ ",
    "|_|",
    " _|"
]

zero = [
    " _ ",
    "| |",
    "|_|"
]

a = [
    " _ ",
    "|_|",
    "| |"
]

b = [
    " _ ",
    "|_\\",
    "|_/"
]

c = [
    " _ ",
    "|  ",
    "|_ "
]

d = [
    " _ ",
    "| \\",
    "|_/"
]

e = [
    " _ ",
    "|_ ",
    "|_ "
]

f = [
    " _ ",
    "|_ ",
    "|  "
]


digits = [zero, one, two, three, four, five, six, seven, eight, nine]
digits_hex = [zero, one, two, three, four, five, six, seven, eight, nine, a, b, c, d, e, f]


translation = []
translation_dict = {}
for h in range(16):
    number = []
    for i in range(3):
        for j in range(3):
            if digits_hex[h][i][j] == " ":
                number.append(0)
            if digits_hex[h][i][j] == "|":
                number.append(1)
            if digits_hex[h][i][j] == "_":
                number.append(2)
            if digits_hex[h][i][j] == "\\":
                number.append(3)
            if digits_hex[h][i][j] == "/":
                number.append(4)
    translation.append(number)
#translation_dict[h] = translation

#print(translation)

# list to convert

# Short hand constructor of the dict class
translation_dict = {}
for index, value in enumerate(translation):
    translation_dict[index] = value

print(translation_dict)



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

print(" --------------- " + str(number_in_digits))
for i in range(9):
    x = number_in_digits[i]
    print(x)
    if x == 0:
        x = 1
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        x = 2
        print(number_in_digits)
        if number_in_digits in translation:
            print("yeay")
            possibilities.append(number_in_digits)
        x = 0

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
#return account