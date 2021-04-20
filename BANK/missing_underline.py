import digits


test = [
    "   ",
    "| |",
    "  |"
]


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

'''
    if x == 0:
        print("x " + str(x))
        x = 1
        print("x " + str(x))
        print("number" + str(number_in_digits))
        print("number in digits " + str(number_in_digits))
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 2
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 0
    
    if x == 1:
        x = 0
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 2
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 1 

    if x == 2:
        x = 1
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 0
        if number_in_digits in digits.translation:
            posiibilities.append(number_in_digits)
        x = 2
    
print(posiibilities)

'''