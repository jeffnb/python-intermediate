def fibonacci():
    '''
    defined as a normal function, but...
    ...no return keyword

    The yield keyword returns a value, but the function retains its state
    '''
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fibonacci()
print(next(f), next(f), 'before the for loop', sep='\n')

import random

random.seed()

for num in f:
    print(num, end=' ')
    if random.random() > 0.95:
        break