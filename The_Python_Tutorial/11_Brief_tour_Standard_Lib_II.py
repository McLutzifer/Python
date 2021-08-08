import reprlib, pprint, textwrap, locale, time, os.path, struct
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
t = Template('return the $item to $owner.')
d = dict(item = 'unladen swallow')


photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

'''
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

p = BatchRename(fmt)
date = time.strftime('%d%b%y')

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = p.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# e.g. insert Ashley_%n%f

'''

# Logging
import logging

print(logging.debug('Debugging Information'))


# Weak References

import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)           # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a    # does not create a reference
print(d['primary']) # fetch the object if it is still alive
del a 
gc.collect()        # run garbge collection right away

# print(d['primary']) # entry was automatically removed   -> Error
