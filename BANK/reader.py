from digits import *


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
    except:
        print("An Error occured - unable to read file")

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
            if single in digits_hex:
                #print("BIS HIRE HER GEHTS MAL")
                check = digits_hex.index(single)
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
    single_digits = digits_hex

    if x in single_digits:
        derived_number = (single_digits.index(x))
        # user story 3
    else:
        derived_number = "?"   # if number is unreadable a "?" will be printed insteead
        #derived_number = missing.missing_piece(x)

    return derived_number