import reader


######################
#    USER STORY 1    #
######################


# my_test_file = "/home/lukas/Documents/Programming/Python
# /BANK/New_try/testfile.txt"

my_test_file = "testfile.txt"


read_digits = reader.read_file(my_test_file)

account_numbers = reader.parse_dictionary(read_digits)

# print(account_numbers)
