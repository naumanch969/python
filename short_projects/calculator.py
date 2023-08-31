import sys

def add(a,b): return a+b

def sub(a,b): return a-b

def mult(a,b): return a*b

def div(a,b): return a/b

def get_numbers():
    first = int(input('Your first number? '))
    second = int(input('Your first number? '))
    return first,second

print('Calculator:')

print('A - Addition')
print('B - Subtraction')
print('C - Mutlitplication')
print('D - Division')
print('Q - Quit')
while True:
    choice = input('Input your choice: ')

    match choice:
        case 'A' | 'a':
            first,second =  get_numbers()
            print(add(first,second))
        case 'B' | 'b':
            first,second =  get_numbers()
            print(sub(first,second))
        case 'C' | 'c':
            first,second =  get_numbers()
            print(mult(first,second))
        case 'D' | 'd':
            first,second =  get_numbers()
            print(div(first,second))
        case 'Q' | 'q':
            sys.exit()
    