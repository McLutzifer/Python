import translator
import sys
import digits

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
        row_of_numbers = []

        line_1 = dic[index+1]
        line_2 = dic[index+2]
        line_3 = dic[index+3]
            
        while position < 33:       # 27 characters + 9 spaces = 36 digits 
            single = []
            
            single.append(line_1[position:position+3])
            single.append(line_2[position:position+3])
            single.append(line_3[position:position+3])

            ######  import hexadecimal translated in digits
            # single to translator
            ## compare
            
            single = translator.translate(single) 
            

            if single in digits.translation:    # check if single is value in translation_dic and if yes return key
                check = digits.translation.index(single)
                row_of_numbers.append(check)
                position += 4
                print("ABER BIS HIER HER")
            else:
                #########  TRY TO FIND WHAT IT IS
                print("bis hier her geht'S")
                pass
                ''' alternatives.illegible() '''
                #check = "?"
                #position += 4
                #row_of_numbers.append(check)
                #missing.missing_piece(single, row_of_numbers) 

        index += 4

        #####
        if '?' in row_of_numbers:
            row_of_numbers.append( "ILL")
        #####
        all_accounts.append(row_of_numbers)

    return all_accounts      # return a list of lists with all accountnumbers from file
