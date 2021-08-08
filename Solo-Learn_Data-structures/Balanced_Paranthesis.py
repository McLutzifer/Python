def balanced(expression):
    
    paranthesis = []
    sum = 0

    for letter in expression:
        if letter == "(":
            sum += 1
            paranthesis.append(letter)
        elif letter == ")":
            sum -= 1
            if paranthesis[-1] == "(":
                paranthesis.pop()
            else:
                return 'False'
    
    if sum == 0:
        return 'True'
    else:
        return 'False'


test1 = '(ui)((uiuisdfds(df(dssds))))'
test2 = '(sdfdsfsd(dsfsfsd((sdfdsf())))'
test3 = ') dsfdsf () ('

balanced(test1)
balanced(test2)
balanced(test3)