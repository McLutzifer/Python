#################################
#         USER STORY 1          #
#################################

line_1 = "     _   _       _   _   _   _   _   _  "
line_2 = "  |  _|  _| |_| |_  |_    | |_| |_| | | "
line_3 = "  | |_   _|   |  _| |_|   | |_|  _| |_| "

# not quickest solution or most efficient but in my opinion easiest way to rad it - understand it by others

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

line = 0 # starting at first line and inspecting 3 at a time

'''

collect all account numbers in a set(!!) (not list because space memory etc) or save it to a txt file...


starting at row 0  line=0
next one is line+4 
EOF? check if exist?



file =open('data.txt','r')
pos =0
while True:
  data = file.read(1)
  if not data:
    break
  pos=pos+1
  file.seek(pos)
  print(data, end='')

file.close()
'''

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
        # user story 3
        else:
            row_of_numbers.append("?")   #####??????????

    i += 4

print(row_of_numbers)
print("Test")





#################################
#         USER STORY 2          #
#################################

checksum = 0
position = 1
while position < 9:
    checksum += position * row_of_numbers[9 - position]
    position +=1

checksum = checksum % 11

if checksum == 0:
    print("YEAY")
else:
    print("NO NO")

