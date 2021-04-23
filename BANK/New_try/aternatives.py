import digits

#################################
possible_alternatives = { 0: [8], 1: [7], 2: [], 
3: [9], 4: [], 5: [6, 9], 6: [5, 8], 
7: [1], 8: [0, 6, 9], 9: [5, 8]}
##################################

def wrong_checksum():
    pass

def illegible(single):
    for i in range(len(single)):    # 9?
        temp_copy = single.copy()                # checks when one single symbol is replaced, if whole 3x3 represents a number 
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