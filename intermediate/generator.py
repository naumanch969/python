# def mygenerator():
#     print('first')
#     yield 1
#     print('second')
#     yield 2
#     print('third')
#     yield 3

# g = mygenerator()
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# print(sum(g))
# print(sorted(g))

# def countdown(num):
#     print('starting')
#     while num > 0:
#         yield num
#         num-=1

# cd = countdown(4)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)


# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums


# def firstn_gen(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# import sys
# mylist = firstn(10000)
# mylist_gen = firstn_gen(10000)
# print(sys.getsizeof(mylist))
# print(sys.getsizeof(mylist_gen))


# def faboncci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a+b

# fib = faboncci(50)
# for i in fib:
#     print(i)

import sys
mygenerator = {i for i in range(1000) if i % 2 == 0}
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))