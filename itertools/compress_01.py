

from pprint import pprint
import itertools


def vowel(c):
	return c.lower() in 'aeiou'

pprint(list(filter(vowel, 'Aardvark')))

pprint(list(itertools.filterfalse(vowel, 'Aardvark')))

pprint(list(itertools.takewhile(vowel, 'Aardvark')))

pprint(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))

pprint(list(itertools.islice('Aardvark', 4)))

pprint(list(itertools.islice('Aardvark', 4, 7)))

pprint(list(itertools.islice('Aardvark', 1, 7, 2)))


print('*' * 50)
sample = [5,4,2,8,7,6,3,0,9,1]
# pprint(list(itertools.accumulate(sample)))

pprint(list(itertools.accumulate(sample, min)))

pprint(list(itertools.accumulate(sample, max)))

import operator

pprint(list(itertools.accumulate(sample, operator.mul)))

pprint(list(itertools.accumulate(range(1, 11), operator.mul)))
