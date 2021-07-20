#########################
#   List comprehension  #
#########################

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)


#########################
#         Tuples        #
#########################

t = 12345, 54321, 'hello!'
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u[1][2])


#########################
#          Sets         #
#########################

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)



#########################
#     Dictionaries      #
#########################

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)