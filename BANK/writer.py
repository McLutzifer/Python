def write_file(account):

#    print(account)
    
    f = open("account_numbers.txt", "a")

    for digit in account:
        digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()
    