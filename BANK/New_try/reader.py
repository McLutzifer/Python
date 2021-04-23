import translator
import sys
import digits
import writer
import checksum


def error_input(text):
    print(text)
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
                error_input("unexpected number on lines")
    except:
        error_input("An Error occured - unable to read file")

    return read_lines







def parse_dictionary(dic):

    all_accounts = []
    index = 0

    while (index + 4) < len(dic):
        position = 0
        row_of_numbers = []     # one list for signs in digits
        account_numbers = []    # onelist for actual accounts to print to file

        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            
        while position < 33:       # 27 characters + 9 spaces = 36 digits 
            single = []
            
            single.append(line_1[position:position+3])
            single.append(line_2[position:position+3])
            single.append(line_3[position:position+3])
           
            single = translator.translate(single) 
            
            if single in digits.translation:    # check if single is value in translation_dic and if yes return key
                check = digits.translation.index(single)
                row_of_numbers.append(check)
                #account_numbers.append()
                position += 4
                #writer.writefile("Accountnumbers_as_read.txt")

            else:
                #########  TRY TO FIND WHAT IT IS            
                ''' alternatives.illegible() '''
                check = "?"
                position += 4
                #row_of_numbers.append(check)
                #missing.missing_piece(single, row_of_numbers) 

    # print out account numbers to file like in Part 3
        if '?' in account_numbers:
            account_numbers.append(" ILL")
            # illegibl    -> add to second file

        else:
            if checksum.checksum == False:
                account_numbers.append(" ERR")

        writer.write_file("Accountnumbers_as_read.txt", account_numbers)

        index += 4
        #####

    

    return all_accounts      # return a list of lists with all accountnumbers from file
