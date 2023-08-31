# name = input("what's your name? ")
# file = open("names.txt","a")
# file.write(f'{name}\n')
# file.close()



# name = input("what's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")


# with open('names.txt','r') as file:
#     lines = file.readlines()
#     for line in lines:
#         # print(line, end='')
#         print(line.rstrip())


# with open('names.txt','r') as file:
#     for line in file:
#         print('hello, ', line.rstrip())


# names = []
# with open('names.txt') as file:
#     for line in file:
#         names.append(line.rstrip())
# for name in sorted(names):
#     print(f'hello, {name}')


# with open('names.txt','r') as file:
#     for line in sorted(file, reverse = True):
#         print('hello, ', line.rstrip())


# with open('students.csv') as file:
#      for line in file:
#         name, house = line.rstrip().split(',')
#         print(f'{name} is in {house}')


# students = []
# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         students.append(f'{name} is in {house}')

# for student in sorted(students):
#     print(student)


# students = []
# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {"name":name, "house":house}
#         students.append(student)

# for student in sorted(students,key=lambda student: student['name']):
#     print(f'{student["name"]} is in {student["house"]}')


# import csv
# students = []
# with open('students.csv') as file:
#     # reader = csv.reader(file)     # return list
#     reader = csv.DictReader(file)       # return dictionary
#     for row in reader:
#         students.append({"name":row['name'], "home":row['home']})

# for student in sorted(students,key=lambda student: student['name']):
#     print(f'{student["name"]} is in {student["home"]}')



# import csv
# name = input("what's your name? ")
# home = input("where's your home? ")

# with open('students.csv','a') as file:
#     # writer = csv.writer(file)
#     writer = csv.DictWriter(file, fieldnames=["name","home"])
#     # writer.writerow([name,home])
#     writer.writerow({"name":name,"home":home})


import sys
from PIL import Image
images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
images[0].save(
    'costume.gif',
    save_all=True,
    append_images=[images[1]],
    duration=100,
    loop=0
)