import digits

#################################
possible_alternatives = { 0: [8], 1: [7], 2: [], 
                        3: [9], 4: [], 5: [6, 9], 6: [5, 8],
                        7: [1], 8: [0, 6, 9], 9: [5, 8]}

possible_alternatives_hex = {0: [8], 1: [7], 2: [], 3: [9], 4: [], 5: [6, 9],
                            6: [5, 8, 15], 7: [1], 8: [0, 6, 9, 10], 9: [5, 8], 10: [8], 11: [13],
                            12: [], 13: [11], 14: [], 15: [6], 16: []}
##################################



def illegible(account, questionmark):
    # if questionmark == 0 ERR justwrong checksum check all numbers
    position = account.index('?')

    possibilities = []

    copies = digits.translation.copy()
    for copy in copies:
        #temp = questionmark

        for i in range(len(copy)):
            x = copy[i]
            for num in range(5):
                copy[i] = num      #replace one digit of copy and see if it matches with ?
                if copy == questionmark:
                    possibilities.append(copy)
            copy[i] = x

    # unique stuff
    if len(possibilities) == 1:
        account[position] = possibilities[0]
        return account                   
    elif len(possibilities) == 0:
        account.append(" ILL")
        return account
    else:
        account.append(" AMB " + str(possibilities))    # forgot first check id checksum is correct


account_test = [1,8,9,4,3,0,'?',6]
questi = [0,2,0,0,2,1,0,0,1]    # should be 7



# for debugging only
illegible(account_test, questi)





def wrong_checksum(single):
    pass
    '''
    possibilities = []
    for i in range(9):  # len(account number)
        temp_copy = single.copy()




    #for i in range(len(single)):   # 9?
    for i in range(9):     #len(single)
        temp_copy = single.copy()       # checks when one single symbol is replaced, if whole 3x3 represents a number 
        #x = number_in_digits[i]
        for num in range(5):
            temp_copy[i] = num
            
            for trans in digits.translation:
                if temp_copy == trans:
                    possibilities.append(single)
                x = num

    unique = [] 
    [unique.append(x) for x in possibilities if x not in unique]


    if len(unique) == 1:
        return unique[0]
    elif len(unique) == 0:
        return '?'
    else:
        # go to checksum 
        pass
    '''