import time

f = open('shoes.txt')

title = ['brand', 'color', 'size']

results = []

elements = f.readlines()

for element in elements:
    lines = element.strip().split()
    results.append({
        'brand': lines[0],
        'color': 'black',
        'size': lines[-1]
    })

print(results)

print('\n')

import time

time.time()

from time import time

time()

from time import time as t

t()
