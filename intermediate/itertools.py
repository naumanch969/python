# itertools: product, permutations, combinations, accumulate, groupby and infinite itertools

# from itertools import product
# a = [1,3]
# b = [2]
# prod = product(a,b, repeat=2)
# print(list(prod))

# permutations
# from itertools import permutations
# a = [1,2,3,4]
# perm = permutations(a,2)
# print(list(perm))

# combinations
# from itertools import combinations, combinations_with_replacement
# a = [1,2,4]
# comb = combinations(a,2)
# comb = combinations_with_replacement(a,2)
# print(list(comb))

# accumlate
# from itertools import accumulate
# import operator
# a = [1,2,3,4]
# acc = accumulate(a, func=operator.mul)
# print(a)
# print(list(acc))

# groupby
# from itertools import groupby
# a = [1,2,3,4]
# groupobj = groupby(a, key=lambda x: x<2)
# persons = [
#     {'name':'Tim','age':54},
#     {'name':'Lisa','age':24},
#     {'name':'John','age':22},
#     {'name':'Clair','age':24}
# ]
# groupobj = groupby(persons, key=lambda x:x['age'])
# for key,value in groupobj:  print(key,list(value))
# print(list(groupobj))

# infinite iterators
from itertools import count, cycle, repeat
# for i in count(10): print(i)
# a = [1,2,3,4]
# for i in cycle(a): print(i)
# for i in repeat(1,10000): print(i)