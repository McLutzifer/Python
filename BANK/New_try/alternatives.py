import checksum
import digits
import translator

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
        account.append(" AMB " + str(possible_accounts))
        return account