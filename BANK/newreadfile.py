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

    row_of_numbers = []
    input_line= 0 # starting at first line and inspecting 3 at a time
    i = 0
    
    ###########  first one "line" by actually "4 lines"
    
    index = 0
    while (index + 4) < len(dic):
        print("")
        
        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            

        while i < 33:       # 27 characters + 9 spaces = 36 digits 
            temp = []
            

            temp.append(line_1[i:i+3])
            temp.append(line_2[i:i+3])
            temp.append(line_3[i:i+3])
    
            print("+++++++++++++++++")
            print(temp)
            print("*****************")
            
            i += 4
            row_of_numbers.append(temp)
        index += 4

    single_digits = digits.digits
    for number in single_digits:
        if temp == number:
            row_of_numbers.append(single_digits.index(number) +1)
        # user story 3
        else:
            row_of_numbers.append("?")   #####??????????


    for row in row_of_numbers:
        print(row)
    return row_of_numbers


    

            
    

####################################################################
def read_lines():
    return 0




##############################
###          TEST

read_digits = read_file(filename)

parse_dictionary(read_digits)

