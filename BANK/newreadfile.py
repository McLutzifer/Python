import digits
import sys
#import exception.error
filename = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"

###################################################################
def error_input():
    print("an ERROR occured - unexpected number on lines")
    sys.exit()

#######################################################################
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

###########################################################################
def parse_dictionary(dic):

    all_accounts = []
    row_of_numbers = []
    #input_line= 0 # starting at first line and inspecting 3 at a time
    position = 0
    #single_digits = digits.digits
    
    ###########  first one "line" by actually "4 lines"
    
    index = 0
    while (index + 4) < len(dic):
        print("")
        
        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            
        while position < 33:       # 27 characters + 9 spaces = 36 digits 
            temp = []
            
            temp.append(line_1[position:position+3])
            temp.append(line_2[position:position+3])
            temp.append(line_3[position:position+3])
    
            print("+++++++++++++++++")
            print(temp)
            print("*****************")
            
            check = check_if_actual_number(temp)
            print(check)

            position += 4
            row_of_numbers.append(check)
        index += 4
        all_accounts.append(row_of_numbers)


    for row in row_of_numbers:
        print(row)



    for c in all_accounts:
        print(c)
        
    return row_of_numbers


def check_if_actual_number(x):
    single_digits = digits.digits

    if x in single_digits:
        derived_number = (single_digits.index(x) +1)
        # user story 3
    else:
        derived_number = "?"

    return derived_number
            
    

####################################################################
def read_lines():
    return 0




##############################
###          TEST

read_digits = read_file(filename)

parse_dictionary(read_digits)

