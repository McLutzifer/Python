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
for h in range(16):     # 'translating' underscores and pipes in integer values for easier comparison 
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

translation_dict = {}
for index, value in enumerate(translation):
    translation_dict[index] = value