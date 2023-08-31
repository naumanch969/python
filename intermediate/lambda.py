# lambda arguments: expression

# add10 = lambda x: x + 10 
# print(add10(10))

# mult = lambda x,y : x * y
# print(mult(3,4))

# points  = [(1,2),(7,3),(3,5),(4,2)]
# points_sorted = sorted(points, key=lambda x: x[0] + x[1] )
# print(points)
# print(points_sorted)

# a = [5,5,6,6]
# b = map( lambda x:x * 2, a )
# print(list(b))

# a = [5,6,5,6]
# b = filter( lambda x: x<6, a )
# print(list(b))

from functools import reduce
a = [5,6,5,6]
product = reduce( lambda x,y:x*y, a )
print(product)