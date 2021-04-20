import reader, writer

my_test_file = "/home/lukas/Documents/Programming/Python/BANK/testfile.txt"
read_digits = reader.read_file(my_test_file)
account_numbers = reader.parse_dictionary(read_digits)
#print(account_numbers)
#print("------------------------------------------------")
for account in account_numbers:
    if "?" in account:
        account.append(" ILL")
    elif len(account) != 9:
        print("Sorry, this number is invalid")
    else:
        if " AMB" or " ILL"  not in account:
            checked = checksum(account)
            if checked == False:
                account.append(" ERR")
        possible_solutions = []

for account in account_numbers:
    #account = str(account)
    writer.write_file(account, "account_numbers_as_read.txt")


#for account in account_numbers:
    if " ERR" in account:
        account = wrong_checksum(account)
        writer.write_file(account, "account_numbers_controlled.txt")
    else:
        writer.write_file(account, "account_numbers_controlled.txt")