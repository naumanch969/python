# () 01
class Student:
    def __init__(self,name,house):
        self.name = name 
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError('Missing Name')
        self._name = name

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ['Gryffindor','Slytherin','Ravenclaw','Hufflepuff']:
            raise ValueError('Invalid House')
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')
    return Student(name,house)

if __name__ == '__main__':
    main()












class Student:
    def __init__(self,name,house):
        self.name = name 
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name,house)

        

def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()


















    # operator overloading
# class Vault:
#     def __init__(self,galleons=0,sickles=0,knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts
#     def __str__(self):
#         return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'
#     def __add__(self,other):
#         galleons = self.galleons + other.galleons
#         sickles = self.sickles + other.sickles
#         knuts = self.knuts + other.knuts
#         return Vault(galleons,sickles,knuts)

    

# potter = Vault(5,55,555)
# weasley = Vault(555,55,5)

# # galleons = potter.galleons + weasley.galleons
# # sickles = potter.sickles + weasley.sickles
# # knuts = potter.knuts + weasley.knuts

# total = potter + weasley
# print(total)















# inheritance
# class Wizard:
#     def __init__(self,name):
#         if not name:
#             raise ValueError('Missing Name')
#         self.name = name

# class Student(Wizard):
#     def __init__(self,name,house):
#         super().__init__(name)
#         self.house = house


# class Professor(Wizard):
#     def __init__(self,name,subject):
#         super().__init(name)
#         self.subject = subject


# wizard = Wizard('Albus')
# student = Student('Harry','Gryffindor')
# professor = Professor('Severus','Defense Against the Dark Arts')
