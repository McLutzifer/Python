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
'''
line = 0

num_dic = []

with open("BANK/testfile.txt", 'r') as file:
    lines = file.readlines()

    count = 0
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line))
        num_dic[count] = str(line)