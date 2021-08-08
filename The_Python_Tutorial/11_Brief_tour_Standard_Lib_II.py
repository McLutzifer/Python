import reprlib
import pprint


print(reprlib.repr(set('supercalifragilisticexpialidocious')))

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width = 30)