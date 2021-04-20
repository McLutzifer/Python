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
    
    account.pop()   # remove ILL
    
    print("___________________________")    
    print(account)
    print("OOOOOOOOOOOOOOOOOOOOOOOOOO")

    multiplier = account.index('?')
    print(9-multiplier)

    pass


def wrong_checksum(account):
    number_of_possibilities = {}

    account.pop()     # remove ERR
    print(possible_alternatives[0])

    print(account)

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
    

    #test = [account for ]


    #my_list = ['new item' if i=='old item' else i for i in my_list]