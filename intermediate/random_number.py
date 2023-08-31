# import random
# a = random.random()
# a = random.uniform(1,10)
# a = random.randint(1,10)    # first excluded
# a = random.randrange(1,10)    # last excluded
# a = random.normalvariate(0,1) # mean, standard deviation
# mylist = list('ABCDEFGHIJK')
# a = random.choice(mylist)
# a = random.sample(mylist,3)
# a = random.choices(mylist,k=3)
# random.shuffle(mylist)

# random.seed(1)  # same value will be generated for random.random() and all others
# print(random.random())
# print(random.randint(1,10))

# random.seed(3)
# print(random.random())
# print(random.randint(1,10))





# import secrets
# a = secrets.randbelow(10)   # 10 excluded
# a = secrets.randbits(2)     # 
# mylist = list('ABCDEFGH')
# a = secrets.choice(mylist)
# print(a)


# import numpy as np
# a = np.random.rand(3)
# a = np.random.rand(3,3)
# a = np.random.randint(0,10,3)   # 0=start,10=exluded,3=len(array)
# a = np.random.randint(0,10,(4,3))
# myarr = np.array([1,2,3,4])
# np.random.shuffle(myarr)
# print(myarr)

# np.random.seed(1)
# print(np.random.rand(1,2))
# np.random.seed(1)
# print(np.random.rand(1,2))