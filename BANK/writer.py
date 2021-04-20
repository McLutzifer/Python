def write_file(account, filename):

#    print(account)
    
    f = open(filename, "a")

    for digit in account:
        digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()

    