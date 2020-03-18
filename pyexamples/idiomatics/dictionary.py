import sys
import functools
from collections import defaultdict, ChainMap

"""
from: https://www.youtube.com/watch?v=OSGv2VnC0go

description: for loop
"""

DIVIDER_LEN = 60


def divider(l=DIVIDER_LEN, is_end=False):
    sys.stdout.write("{}".format('-') * DIVIDER_LEN)
    print('')
    if is_end:
        print('')


# Do: looping over dictionary keys
divider()
print("Do: looping over dictionary keys")
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k in d:
    print(k)
print('')

# Do: another way to looping over dictionary keys
print('Do: another way to looping over dictionary keys')
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k in d.keys():
    print(k)
divider(is_end=True)


# Do: looping over dictionary keys and values
divider()
print("Do: looping over dictionary keys and values")
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k in d:
    print(k, '-->', d[k])
print('')

# Do: looping over dictionary keys and values, use items()
divider()
print("Do: looping over dictionary keys and values, use items()")
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
for k, v in d.items():
    print(k, '-->', v)
divider(is_end=True)

# Do: construct a dictionary from paris of lists
divider()
print("Do: construct a dictionary from paris of lists, create tuple of each pairs")
names = {'matthew', 'rachel', 'raymond'}
colors = {'blue', 'green', 'red'}
d = dict(zip(names, colors))
print('d: =>', d)
print('')

# Do: construct a dictionary from paris of lists
divider()
print("Do: construct enumerate dictionary from list")
colors = {'blue', 'green', 'red'}
d = dict(enumerate(colors))
print('d: =>', d)
divider(is_end=True)

# Don't: counting elements of dictionary
divider()
print("Don't: counting elements of dictionary")
colors = ['blue', 'green', 'red', 'black', 'red', 'green', 'green']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print('counting of color:', d)
print('')

# Do: counting elements of dictionary, use get default option
print("Do: counting elements of dictionary, use get default option")
colors = ['blue', 'green', 'red', 'black', 'red', 'green', 'green']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print('counting of color:', d)
print('')

# Do: another option - use defaultdict(int) counting elements of dictionary, use get default option
print("Do: another option - use defaultdict(int) counting elements of dictionary, use get default option")
colors = ['blue', 'green', 'red', 'black', 'red', 'green', 'green']
d = defaultdict(int)    # set to zero if int is alone
for color in colors:
    d[color] += 1
print('counting of color:', d)
divider(is_end=True)

# Don't: grouping with dictionary: part - I
print("Don't: grouping with dictionary: part - I")
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)
print('')

# Do: grouping with dictionary: part - I
print("Do: grouping with dictionary: part - I")
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)
divider(is_end=True)

# Do: is directory popitem() atomic
divider()
print("Do: is directory popitem() atomic")
d = {'raymond': 'red', 'rachel': 'blue', 'matthew': 'black', 'roger': 'yellow'}
while d:
    key, value = d.popitem()
    print(key, '-->', value)
print(d)
divider(is_end=True)

# Do: copying and update several dictionary to one
divider()
d1 = {'d1-arg1': 'd1-val1', 'd1-arg2': 'd1-val2'}
d2 = {'d2-arg1': 'd2-val1', 'd2-arg2': 'd2-val2'}
d3 = {'d3-arg1': 'd3-val1', 'd3-arg2': 'd3-val2'}

d = ChainMap(d1, d2, d3)
print(d)
divider(is_end=True)


