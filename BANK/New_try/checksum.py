def checksum(accountnumber):
    
    checksum = 0
    position = 1

    while position < 10:     
        checksum += position * accountnumber[9 - position]
        position +=1
    
    if checksum % 11 == 0:
        return True
    else:
        return False