def checksum(accountnumber):
    
    checksum = 0
    position = 1

    #first of all check if account number is valid
    #meaning only 9 digits long and no "?"

    while position < 9:
        checksum += position * accountnumber[9 - position]
        position +=1
    
    if checksum % 11 != 0:
        accountnumber.append(" ERR")

    return accountnumber
