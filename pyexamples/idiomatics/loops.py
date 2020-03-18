import sys
import functools

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


# Don't do: cause list on memory
divider()
print("Don't do: list is created on memory")
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
print('')

# Do: range cause it use generator (iterator) python3 -> range, python2 -> xrange
print('Do: range is an iterator (a generator)')
for i in range(6):
    print(i)
divider(is_end=True)

# Do: looping over collection
divider()
print('Do: looping over collection')
for color in ['red', 'green', 'blue', 'yellow']:
    print(color)
print('')

# Do: looping backward
print('Do: looping backward')
for color in reversed(['red', 'green', 'blue', 'yellow']):
    print(color)
divider(is_end=True)

# Don't do: looping over collection with indices
divider()
print("Don't do: looping over collection with indices")
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(i, '-->', colors[i])
print('')

print("Do: looping over collection with indices - use enumeration")
for i, color in enumerate(colors):
    print(i, '-->', color)
divider(is_end=True)

# Don't do: looping over two collections at once
divider()
print("Don't do: looping over two collections at once")
colors = ['red', 'green', 'blue', 'yellow']
names = ['raymond', 'rachel', 'matthew']
n = min(len(names), len(colors));
for i in range(n):
    print(names[i], '-->', colors[i])
print('')

print("Do: use zip - looping over two collections at once")
for name, color in zip(names, colors):
    print(name, '-->', color)
divider(is_end=True)

# Don't do: custom sort order
divider()
print("Don't do: custom sort order, number of comprasion is n(log(n))")
colors = ['red', 'green', 'blue', 'yellow']


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0


print(sorted(colors))
print('')
print('Do: custom sort order - use key')
print(sorted(colors, key=len))
divider(is_end=True)

# Don't do: call function until sentinel value
divider()
print("Don't do: call function until sentinel value")
blocks = []
with open('data.txt') as file:
    while True:
        block = file.readline()
        if block == '\n':
            break
        blocks.append(block)
print(blocks)
print('')

print("Do: call function until sentinel value")
blocks = []
with open('data.txt') as file:
    for block in iter(functools.partial(file.readline), '\n'):
        blocks.append(block)
print(blocks)
divider(is_end=True)

# Don't do: distinguishing multiple exit points in loops
print("Don't do: distinguishing multiple exit points in loops")
colors = ['red', 'green', 'blue', 'yellow']


def find_not_to_do(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


print('find blue in colors is =>', find_not_to_do(colors, 'blue'))
print('find none in colors is =>', find_not_to_do(colors, 'none'))
print('')

# Doo: distinguishing multiple exit points in loops
print("Do: distinguishing multiple exit points in loops - use for - else")


def find_to_do(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i


print('find blue in colors is =>', find_to_do(colors, 'blue'))
print('find none in colors is =>', find_to_do(colors, 'none'))
divider(is_end=True)


