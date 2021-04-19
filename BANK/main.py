import reader, checksum, writer


#################################
#         USER STORY 1          #
#################################


my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"

read_digits = reader.read_file(my_test_file)
account_numbers = reader.parse_dictionary(read_digits)
#print(account_numbers)



#################################
#         USER STORY 2          #
#################################


for account in account_numbers:
    if "?" in account:
        account.append(" ILL")
    elif len(account) != 9:
        print("Sorry, this number is invalid")
    else:
        account = checksum.checksum(account)



print(account_numbers)
#################################
#         USER STORY 3          #
#################################

for account in account_numbers:
    #account = str(account)
    writer.write_file(account)




'''


print(digits.one)


line_1 = "     _   _       _   _   _   _   _   _  "
line_2 = "  |  _|  _| |_| |_  |_    | |_| |_| | | "
line_3 = "  | |_   _|   |  _| |_|   | |_|  _| |_| "

# not quickest solution or most efficient but in my opinion easiest way to rad it - understand it by others





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
'''

'''
def read_file(filename):

    row_of_numbers = []
    line= 0 # starting at first line and inspecting 3 at a time
    i = 0

    ##########
    with open(filename, 'r') as file:
    
    # check if lines in file %4 == 0
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

    return row_of_numbers


def read_lines():
    return 0


#################################
#         USER STORY 2          #
#################################


'''
# see that checksum only works when number of digits is actuall<9 and not 8 + ?
'''
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
'''


#################################
#         USER STORY 3          #
#################################


########################## 3 ######   ??????
#add_on_text = ""
#if checksum != 0:
#    add_on_text = "ERR"
#if len(row_of_numbers) != 9:
#    add_on_text = "ILL"


'''
def get_account_numbers_from_file(filename):
    """Returns all account numbers found in <filename>, as a list of tuples"""

    account_numbers = []

    linecount = 0
    numberlines = ''
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1

            if (linecount % 4) == 0:
                account_numbers.append(parse_account_number(numberlines))
                numberlines = ''
            else:
                # make sure to trim trailing newline
                numberlines += line.rstrip('\n')

    return account_numbers
'''







#################################
#         USER STORY 4          #
#################################

# if account numbree containing ERR or ILL

# one underscore missing: 
# 1=7
# 0=8
# one pipe missing
# 3=9
# 5=9
# 5=6
# 6=8
# 9=8









#################################
#         USER STORY 5          #
#################################

