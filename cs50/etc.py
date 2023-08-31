# yell('this','is','CS50')

# def yell(*words):
#     # uppercased = map(str.upper, words )
#     uppercased = [word.upper() for word in words]
#     print(*uppercased)


# students = [
#     {'name':'harry','house':'Gryffindor'},
#     {'name':'hermoine','house':'Gryffindor'},
#     {'name':'ron','house':'Gryffindor'},
#     {'name':'draco','house':'Slytherin'},
# ]
#  # gryffindors = [ student['name'] for student in students if student['house'] == 'Gryffindor' ]
# gryffindors = filter(lambda student:student['house'] == 'Gryffindor' ,students)



# students = ['ron','harry','hermoine']
# gryffindors = {student:'Gryffindor' for student in students}


# students = ['ron','harry','hermoine']
# for i,student in enumerate(students):
#     print(i+1,student)




def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield 's' * i
if __name__ == '__main__':
    main()