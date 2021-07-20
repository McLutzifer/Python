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

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    print('---------')

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 53.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)



#########################
#      Conditions       #
#########################

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)