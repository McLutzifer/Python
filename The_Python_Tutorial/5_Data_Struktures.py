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

a = {x for x in 'abracadabra'}
print(a)