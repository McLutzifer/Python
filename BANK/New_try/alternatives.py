import checksum
import digits
import translator

#################################
possible_alternatives = { 0: [8], 1: [7], 2: [], 
                        3: [9], 4: [], 5: [6, 9], 6: [5, 8],
                        7: [1], 8: [0, 6, 9], 9: [5, 8]}

possible_alternatives_hex = {0: [8], 1: [7], 2: [], 3: [9], 4: [], 5: [6, 9],
                            6: [5, 8, 15], 7: [1], 8: [0, 6, 9, 10], 9: [5, 8], 10: [8], 11: [13],
                            12: [], 13: [11], 14: [], 15: [6], 16: []}
##################################



def check_possibilities(to_check):
    possibilities = []
    for element in digits.translation:
        copy = to_check.copy()
        for i in range(len(to_check)):
            for num in range(5):
                save = copy[i]
                copy[i] = num
                if copy == element:
                    possibilities.append(copy.copy())
                copy[i] = save
    return possibilities

# questionmark = [0, 2, 0, 0, 2, 1, 0, 0, 1]

# account_test = [1,8,9,4,3,0,'?',6]
# questi = [0,2,0,0,2,1,0,0,1]    # should be 7
questi = [0,2,0,0,0,1,0,0,1]
# ### for debugging only
# illegible(account_test, questi)
x = check_possibilities(questi)
print(x)

def illegible(account, questionmark):
    position = account.index('?')
    possibilities = check_possibilities(questionmark)

    unique = []
    [unique.append(x) for x in possibilities if x not in unique]

    if len(unique) == 1:
        account[position] = unique[0]
        if checksum.checksum(account) == False:
            account.append(" ERR")
        return account
    elif len(unique) == 0:
        account.append(" ILL")
        return account
    else:
        account.append(" AMB => " + str(unique))    # forgot first check id checksum is correct
        return account

# account_test = [1,8,9,4,3,0,'?',6]
# questi = [0,2,0,0,2,1,0,0,1]    # should be 7
# ### for debugging only
# illegible(account_test, questi)


def wrong_checksum(account):

    possible_accounts = []

    for i in range(len(account)):
        index = account[i]
        hex = digits.digits_hex[index]
        to_check = translator.translate(hex)
        possibilities = check_possibilities(to_check)

        possible_digits = []

        if(len(possible_digits)) == 0:
            break

        for entry in possibilities:
            if entry in digits.digits_hex:
                possible_digits.append(digits.digits_hex.index())

        temp = account.copy()
        for j in possible_digits:
            temp[i] = j
            if checksum.checksum(temp) == True:
                possible_accounts.append(temp)



    if len(possible_accounts) == 1:
        account= possible_accounts[0]
        return account
    elif len(possible_accounts) == 0:
        account.append(" ERR")
        return account
    else:
        account.append(" AMB " + str(possible_accounts))    # forgot first check id checksum is correct
        return account