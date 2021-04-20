import checksum

possible_alternatives = { 0: [8], 1: [7], 2: [], 3: [9], 4: [], 5: [6, 9], 6: [5, 8], 7: [1], 8: [0, 6, 9], 9: [5, 8] }

def possible_outcomes(account, list_of_possibilities):

    if len(list_of_possibilities) == 1:
        return list_of_possibilities[0]

    elif len(list_of_possibilities) == 0:
        account.append(" ILL")
        return account
    else:
        account.append(" AMB =>")
        account.append(list_of_possibilities)
        return account


def wrong_checksum(account):
    list_of_possibilities = []

    account.pop()     # remove ERR
    possible_account = account.copy()

    for i in range(len(possible_account)):
        for entry in possible_alternatives[possible_account[i]]:
            actual_number = possible_account[i]
            possible_account[i] = entry

            if checksum.checksum(possible_account) == True:
                to_add=possible_account.copy()
                list_of_possibilities.append(to_add)

            possible_account[i] = actual_number

    account = possible_outcomes(account, list_of_possibilities)
    return account
