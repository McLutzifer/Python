

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
    number_of_possibilities = 0
    
    account.pop()
    
    print("___________________________")    
    print(account)
    print("OOOOOOOOOOOOOOOOOOOOOOOOOO")

    multiplier = account.index('?')
    print(9-multiplier)


def wrong_checksum(account):
    pass
    
    