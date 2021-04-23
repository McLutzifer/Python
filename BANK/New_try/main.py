import parser
import sys


def error_input(text):
    print(text)
    sys.exit()


######################
#    USER STORY 1    #
######################


# my_test_file = "/home/lukas/Documents/Programming/Python
# /BANK/New_try/testfile.txt"

my_test_file = "testfile.txt"


read_digits = {}
try:
    with open(my_test_file, 'r') as file:
        lines = file.readlines()

        count = 0
        for line in lines:
            count += 1
            read_digits[count] = line

        #if len(read_lines) %4 != 0:
            #error_input("unexpected number on lines")
except:
    error_input("An Error occured - unable to read file")

        #if len(read_lines) %4 != 0:
            #error_input("unexpected number on lines")



#read_digits = reader.read_file(my_test_file)

account_numbers = parser.parse_dictionary(read_digits)

# print(account_numbers)
