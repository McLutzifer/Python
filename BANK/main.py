import reader, writer, wrong_checksum, checksum

######################
#    USER STORY 1    #
######################

my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"
read_digits = reader.read_file(my_test_file)
account_numbers = reader.parse_dictionary(read_digits)

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
            checked = checksum.checksum(account)
            if checked == False:
                account.append(" ERR")
        possible_solutions = []

######################
#    USER STORY 3    #
######################
for account in account_numbers:
    writer.write_file(account, "account_numbers_as_read.txt")


######################
#    USER STORY 4    #
######################
    if " ERR" in account:
        account = wrong_checksum.wrong_checksum(account)
        writer.write_file(account, "account_numbers_controlled.txt")
    else:
        writer.write_file(account, "account_numbers_controlled.txt")