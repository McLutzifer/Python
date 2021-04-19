def write_file(account):

#    print(account)
    
    f = open("account_numbers.txt", "w")

    for digit in account:
        digit = str(digit)
        #f.write(digit)
        print(str(digit))
    #f.write("\n")
    f.close()
    