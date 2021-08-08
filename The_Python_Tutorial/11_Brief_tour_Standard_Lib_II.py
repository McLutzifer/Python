import reprlib, pprint, textwrap, locale
from string import Template

print(reprlib.repr(set('supercalifragilisticexpialidocious')))

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)

doc = """The wrap() method is just like fill() except that it returns
 a list of strings instead of one big string with newlines to separate
 the wrapped lines."""
print(textwrap.fill(doc, width = 40)) 

#locale.setlocale(locale.LC_ALL, 'English_United States.1252')
#conv = locale.localeconv()    # get a mapping of conventions

# Templating

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause = 'the ditch fund'))