
import sys

def checksum(accountnumber):
    
    checksum = 0
    position = 1

    while position < 10:     
        checksum += position * accountnumber[9 - position]
        position +=1
    
    if checksum % 11 == 0:
        return True
    else:
        return False

##################################
#             DIGITS         #
##################################






######################
#    USER STORY 1    #
######################


my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"
#read_digits = reader.read_file(my_test_file)
#my_test_file = "BANK/testfile.txt"


read_lines = {}
try:
    with open(my_test_file, 'r') as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            count += 1
            read_lines[count] = line

        #if len(read_lines) %4 != 0:
            #error_input()
except:
    print("An Error occured - unable to read file")

#return read_lines

#account_numbers = reader.parse_dictionary(read_digits)

possible_alternatives = { 0: [8], 1: [7], 2: [], 
3: [9], 4: [], 5: [6, 9], 6: [5, 8], 
7: [1], 8: [0, 6, 9], 9: [5, 8]}

def missing(to_check):

    return to_check

dic = read_lines
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
        
        if single in digits_hex:
            check = digits_hex.index(single)
            position += 4
            row_of_numbers.append(check)
        else:
            check = "?"
            position += 4
            row_of_numbers.append(check)
            #missing.missing_piece(single, row_of_numbers) 
        integer = single
        account = row_of_numbers
        ##############################################
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

            for i in range(len(number_in_digits)):  
                temp_copy = number_in_digits.copy()                # checks when one single symbol is replaced, if whole 3x3 represents a number 
                #x = number_in_digits[i]
                for num in range(5):
                    temp_copy[i] = num
                    
                    for trans in translation:
                        if temp_copy == trans:
                            possibilities.append(number_in_digits)
                        x = num

            unique = [] 
            [unique.append(x) for x in possibilities if x not in unique]
            #account = wrong_checksum.possible_outcomes(integer, unique)
            #----------------------------------------------------------
            list_of_possibilities = []

            #account.pop()     # remove ERR
            #possible_account = account.copy()

            for i in range(len(unique)):
                if checksum(unique[i]) == True:
                    list_of_possibilities.append(unique[i])

            '''
            for i in range(len(possible_account)):
                for entry in possible_alternatives[possible_account[i]]:
                    actual_number = possible_account[i]
                    possible_account[i] = entry

                    if checksum(possible_account) == True:
                        to_add=possible_account.copy()
                        list_of_possibilities.append(to_add)

                    possible_account[i] = actual_number
            '''
            #account = possible_outcomes(account, list_of_possibilities)
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

            if len(list_of_possibilities) == 1:
                account =  list_of_possibilities[0]

            elif len(list_of_possibilities) == 0:
                account.append(" ILL")
                #return account
            else:
                account.append(" AMB =>")
                account.append(list_of_possibilities)
                #return account
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #return account
            #----------------------------------------------------------
            #return account
            ###############################################

    index += 4
    all_accounts.append(row_of_numbers)

#return all_accounts      # return a list of


account_numbers = all_accounts


######################
#    USER STORY 2    #
######################

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


######################
#    USER STORY 3    #
######################
for account in account_numbers:
    #writer.write_file(account, )
    f = open("account_numbers_as_read.txt", "a")

    for digit in account:
        digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()


######################
#    USER STORY 4    #
######################
    if " ERR" in account:
        #account = wrong_checksum.wrong_checksum(account)

        list_of_possibilities = []

        account.pop()     # remove ERR
        possible_account = account.copy()

        for i in range(len(possible_account)):
            if possible_account[i] < 10:
                for entry in possible_alternatives[possible_account[i]]:
                    actual_number = possible_account[i]
                    possible_account[i] = entry

                    if checksum(possible_account) == True:
                        to_add=possible_account.copy()
                        list_of_possibilities.append(to_add)

                    possible_account[i] = actual_number
            else:
                pass

        #account = possible_outcomes(account, list_of_possibilities)
        #return account
        if len(list_of_possibilities) == 1:
            account = list_of_possibilities[0]

        elif len(list_of_possibilities) == 0:
            account.append(" ILL")
            #return account
        else:
            account.append(" AMB =>")
            account.append(list_of_possibilities)
            #return account

        f = open("account_numbers_controlled.txt", "a")

        for digit in account:
            digit = str(digit)
            f.write(digit)
        f.write("\n")
        f.close()

        #writer.write_file(account, "account_numbers_controlled.txt")
    else:
        #writer.write_file(account, "account_numbers_controlled.txt")
        f = open("account_numbers_controlled.txt", "a")

        for digit in account:
            digit = str(digit)
            f.write(digit)
        f.write("\n")
        f.close()