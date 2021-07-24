
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