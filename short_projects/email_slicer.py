import sys
print('Email Slicer: ')

while True:
    email = input("Your Email? ")

    (username,domain) = email.split('@')
    (domain,extension) = domain.split('.')

    print(f'Username: {username}')
    print(f'Domain: {domain}')
    print(f'Extension: {extension}')

    question = input('wanna continue? (y for yes, n for no): ')
    if question == ('n' or 'N'): sys.exit()