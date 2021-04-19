def write(account):

#    print(account)
    
    f = open("account_numbers.txt", "a")

    for digit in account:
        f.write(digit)
    f.write("\n")
    f.close()
    