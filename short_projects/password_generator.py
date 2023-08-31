import string
import random

def main():
    option = input('Wanna create a password? ')
    if option == ('y' or 'Y'): 
        length = int(input('Enter the length of password: '))
        print('Your password is: ',generate_password(length))
    else:
        pass


def generate_password(length):
    characters = list(string.ascii_letters + string.digits + '!@#$%^&*')
    password = []
    for _ in range(length): password.append(random.choice(characters))
    random.shuffle(password)
    return str(''.join(password))

if __name__ == '__main__':
    main()