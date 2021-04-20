
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


##################################
#           MISSING          #
################################



#test = [    "   ",    "| |",     "  |" ]


def missing_piece(integer, account):     ##### MISSING PIECE STUFF  add account

    possibilities = []

    #integer = ["   ","| |", "  |"]   #verwortackelter vierer
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
            number_in_digits[i] = 1
            print(number_in_digits)
            if number_in_digits in translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 2
            print(number_in_digits)
            if number_in_digits in translation:
                print("yeay")
                possibilities.append(number_in_digits)
            number_in_digits[i] = 0

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
    return account
  


#################################
#         READER       #
#################################


my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"


def error_input():
    print("an ERROR occured - unexpected number on lines")
    sys.exit()

def read_file(filename):
    read_lines = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    
            count = 0
            for line in lines:
                count += 1
                read_lines[count] = line
    
            if len(read_lines) %4 != 0:
                error_input()
    except Exception as e:
        #exception.error.logger.error(e)
        pass
    #print(len(read_lines))
    return read_lines

def parse_dictionary(dic):

    all_accounts = []

    index = 0
    while (index + 4) < len(dic):
        position = 0
        row_of_numbers = []

        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            
        while position < 33:       # 27 characters + 9 spaces = 36 digits 
            single = []
            
            single.append(line_1[position:position+3])
            single.append(line_2[position:position+3])
            single.append(line_3[position:position+3])
            
            #check = check_if_actual_number(single)############
            ############################
            if single in digits:
                print("BIS HIRE HER GEHTS MAL")
                check = digits.index(single)
                position += 4
                row_of_numbers.append(check)
            else:
                check = "?"
                position += 4
                row_of_numbers.append(check)
                missing_piece(single, row_of_numbers)  ##MISSING PIECE
                ###################################################
                ################################################

            #position += 4
            #row_of_numbers.append(check)
        index += 4
        all_accounts.append(row_of_numbers)

    return all_accounts      # return a list of lists with all acountnumbers from file


def check_if_actual_number(x):
    single_digits = digits

    if x in single_digits:
        derived_number = (single_digits.index(x))
        # user story 3
    else:
        derived_number = "?"   # if number is unreadable a "?" will be printed insteead
        #derived_number = missing.missing_piece(x)

    return derived_number

    
##############################
###          WRITER        #
##########################


def write_file(account, filename):

#    print(account)
    
    f = open(filename, "a")

    for digit in account:
        digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()
    
###########################
#          CHECKSUM     #
########################

def checksum(accountnumber):
    
    checksum = 0
    position = 1

    #first of all check if account number is valid
    #meaning only 9 digits long and no "?"

    while position < 10:
        checksum += position * accountnumber[9 - position]
        position +=1
    
    if checksum % 11 == 0:
        return True
    else:
        return False



   
#####################################
#        WRONG CHECKSUM        #
####################################


possible_alternatives = { 0: [8], 1: [7], 2: [], 3: [9], 4: [], 5: [6, 9], 6: [5, 8], 7: [1], 8: [0, 6, 9], 9: [5, 8] }

def possible_outcomes(account, list_of_possibilities):

    if len(list_of_possibilities) == 1:
        print("################# nothing here")    
        return list_of_possibilities[0]

    elif len(list_of_possibilities) == 0:
        account.append(" ILL")
        print("#############THATS ILL")
        print(account)
        return account
    else:
        account.append(" AMB =>")
        account.append(list_of_possibilities)
        print("####----++++++----------finally")
        return account


def wrong_checksum(account):
    list_of_possibilities = []
    #possibilities = {account: list_of_possibilities}

    account.pop()     # remove ERR
    #print(possible_alternatives[0])

    #print(account)

    possible_account = account.copy()

    for i in range(len(possible_account)):
        for entry in possible_alternatives[possible_account[i]]:
            #print("............................")
            #print(entry)
            #print(".............................")
            actual_number = possible_account[i]
            print("actual_number " + str(actual_number))
            possible_account[i] = entry
            print("possible account[i] " + str(possible_account[i]))
            #print(possible_account)

            if checksum(possible_account) == True:
                print("tha's right: " + str(possible_account)) 
                to_add=possible_account.copy()
                list_of_possibilities.append(to_add)
                print(list_of_possibilities)

            possible_account[i] = actual_number
            print("possible account[i] " + str(possible_account[i]))

    print(list_of_possibilities)

    account = possible_outcomes(account, list_of_possibilities)
    return account


    
#wrong_checksum( [7,1,8,9,9,8,1,0,9, "ERR"])


            

########################
#       WRITER        #
######################

def write_file(account, filename):

#    print(account)
    
    f = open(filename, "a")

    for digit in account:
        digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()
    








#################################
#         MAIN       #
#################################


my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"
read_digits = read_file(my_test_file)
account_numbers = parse_dictionary(read_digits)
print(account_numbers)
print("------------------------------------------------")
for account in account_numbers:
    if "?" in account:
        account.append(" ILL")
    elif len(account) != 9:
        print("Sorry, this number is invalid")
    else:
        if " AMB" or " ILL"  not in account:
            checked = checksum(account)
            if checked == False:
                account.append(" ERR")
        possible_solutions = []

for account in account_numbers:
    #account = str(account)
    write_file(account, "account_numbers_as_read.txt")

for account in account_numbers:
    print(account)

for account in account_numbers:
    if " ERR" in account:
        account = wrong_checksum(account)
        write_file(account, "account_numbers_controlled.txt")
    else:
        write_file(account, "account_numbers_controlled.txt")