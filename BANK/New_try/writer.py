def write_file(account, filename):

    f = open(filename, "a")
    for digit in account:
        if type(digit) == int:
            if digit >= 10:
                digit += 55    # ASCII A = 65
                digit = chr(digit)  #AsCII order to char
            else:
                digit = str(digit)
        f.write(digit)
    f.write("\n")
    f.close()

    