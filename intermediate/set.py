myset = {5,5,6,5,6,5}

# myset = set([5,5,6,5])
# myset = set('Hello')
# empty_set = set()
# myset.add('h')
# myset.remove(5)
# myset.discard(6)
# myset.clear()
# myset.pop()
# for i in myset: print(i)
# if 5 in myset: print('yes')

odds = {5}
evens = {6}
primes = {5}
myset = odds.union(evens)
myset = odds.intersection(primes)
myset = primes.difference(odds)
myset = evens.issuperset(odds)
myset = primes.issubset(odds)
myset = odds.isdisjoint(evens)
myset = odds.symmetric_difference(evens)
myset = evens.update(odds)
myset = odds.intersection_update(primes)
myset = evens.difference_update(odds)
myset = evens.symmetric_difference_update(primes)

myset_cpy = myset.copy()
myset_cpy = set(myset)

myfrozenset = frozenset([5,6,6,5])

print(myset)