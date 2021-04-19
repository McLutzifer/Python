def parse_dictionary(dic):

    row_of_numbers = []
    input_line= 0 # starting at first line and inspecting 3 at a time
    i = 0
    
    ###########  first one "line" by actually "4 lines"
    
    index = 0
    while (index + 4) < len(dic):
        print("")
        
        index += 4

        while i < 33:       # 27 characters + 9 spaces = 36 digits 
            temp = []
            
            line_1 = dic[index+1]
            line_2 = dic[index+2]
            line_3 = dic[index+3]
            
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
