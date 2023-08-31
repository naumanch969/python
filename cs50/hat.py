import random

class Hat:
    houses = ['Gryffindor','Ravonclaw','Slytherin','Hufflepuff']

    @classmethod
    def sort(cls,name):
        print(name, 'is in',random.choice(cls.houses))

Hat.sort('Harry')