import translator

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
for h in range(16):
    number = translator.translate(digits_hex[h])
    translation.append(number)


translation_dict = {}
for index, value in enumerate(translation):
    translation_dict[index] = value

