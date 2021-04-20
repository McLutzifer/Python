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

digits = [zero, one, two, three, four, five, six, seven, eight, nine]



translation = []
for h in range(9):
    number = []
    for i in range(3):
        for j in range(3):
            if digits[h][i][j] == " ":
                number.append(0)
            if digits[h][i][j] == "|":
                number.append(1)
            if digits[h][i][j] == "_":
                number.append(2)
    translation.append(number)
#print(translation)



'''
one_str   = "     |  |"
two_str   = " _  _||_ "
three_str = " _  _| _|"
four_str  = "   |_|  |"
five_str  = " _ |_  _|"
six_str   = " _ |_ |_|"
seven_str = " _   |  |"
eight_str = " _ |_||_|"
nine_str  = " _ |_| _|"
zero_str  = " _ | ||_|"

digits_str = [ one_str, two_str, three_str, 
four_str, five_str, six_str, seven_str, 
eight_str, nine_str, zero_str ]
'''

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

hex = [zero, one, two, three, four, five, six, seven, eight, nine, a, b, c, d, e, f]
