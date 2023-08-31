# Counter
# from collections import Counter
# a = 'aaaaabbbbcccd'
# mycounter = Counter(a)
# print(mycounter.keys())
# print(mycounter.values())
# print(mycounter.most_common(1))
# print(mycounter.most_common(1)[0][0])
# print(list(mycounter.elements()))
# print(mycounter)


# NamedTuple
# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt = Point(1,3)
# print(pt)


# OrderedDict
# from collections import OrderedDict
# ordereddict = OrderedDict()
# ordereddict['b'] = 2
# ordereddict['a'] = 1
# ordereddict['d'] = 4
# ordereddict['c'] = 3
# print(ordereddict)


# DefaultDict
# from collections import defaultdict
# d = defaultdict(int)    # default value of int is default value of dict key 
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# print(d['a'])


# Deque
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.clear()
d.extend([3,4,5,6])
d.rotate(1)
print(d)