line_1 = "     _   _       _   _   _   _   _   _  "
line_2 = "  |  _|  _| |_| |_  |_    | |_| |_| | | "
line_3 = "  | |_   _|   |  _| |_|   | |_|  _| |_| "

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

digits = [one, two, three, four, five, six, seven, eight, nine, zero]

row_of_numbers = []
i = 0
while i < 33:       # 27 characters + 9 spaces = 36 digits 
    temp = []

    temp.append(line_1[i:i+3])
    temp.append(line_2[i:i+3])
    temp.append(line_3[i:i+3])

    for number in digits:
        if temp == number:
            row_of_numbers.append(digits.index(number) +1)

    i += 4

print(row_of_numbers)