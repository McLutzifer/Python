
year = 2016
event = 'Referendum'

print(f'Results of the {year} {event}')


yes_votes = 42_572_654
no_votes = 43_132_495

percentage = yes_votes / (yes_votes + no_votes)

print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))


hello = 'Hello, world\n'
hellos = repr(hello)
print(hellos)


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print('The story of {1}, {0}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926539'.zfill(5))


f = open('workfile', 'w')