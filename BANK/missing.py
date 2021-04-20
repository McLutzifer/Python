from checksum import *

one_pipe_missing = {3: 9, 5: [6,9], 6: 8, 9:8}
underscore_missing = {1:7, 0:8}

possible_alternatives = {
    0: [8],
    1: [7],
    2: [],
    3: [9],
    4: [],
    5: [6, 9],
    6: [5, 8],
    7: [1],
    8: [0, 6, 9],
    9: [5, 8]
    }

def missing_piece(account):
    number_of_possibilities = {}
    '''
    account.pop()   # remove ILL
    
    print("___________________________")    
    print(account)
    print("OOOOOOOOOOOOOOOOOOOOOOOOOO")

    multiplier = account.index('?')
    print(9-multiplier)
'''
    pass


def wrong_checksum(account):
    list_of_possibilities = []
    #possibilities = {account: list_of_possibilities}

    account.pop()     # remove ERR
    print(possible_alternatives[0])

    print(account)

    possible_account = account

    for i in range(len(possible_account)):
        for entry in possible_alternatives[possible_account[i]]:
            print("............................")
            print(entry)
            print(".............................")
            actual_number = possible_account[i]
            possible_account[i] = entry
            print(possible_account)

            if checksum(possible_account) == True:
                print("tha's right: " + str(account)) 
                list_of_possibilities.append(possible_account)

            account[i] = actual_number

    print(list_of_possibilities)
'''
    for number in account:
        for item in possible_alternatives[number]:
            #if item != None:
            print(account)
            print(item)
            saved, number = number, item
            account.replace(number, item)
            print(account)
            if checksum(account) == True:
                number_of_possibilities[saved] = item
            else:
                number = saved

    print("OXOXOXOXOXOXOXOXOOXOXOXOXOXOXO")
    print(number_of_possibilities)
    print("OXOXOXOXOXOXOXOXOOXOXOXOXOXOXO")
    
'''
    #test = [account for ]


    #my_list = ['new item' if i=='old item' else i for i in my_list]