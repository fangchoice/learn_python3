

import itertools

print(list(itertools.chain('abc', range(2))))

print(list(itertools.chain(enumerate('abc'))))

print(list(itertools.chain.from_iterable(enumerate('abc'))))

