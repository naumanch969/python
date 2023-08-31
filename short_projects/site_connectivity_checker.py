import urllib.request as urllib

def main():
    print('Site Connectivity Checker')
    check()

def check():
    url = input('Enter URL: ')

    print('Checking Connectivity....')
    response = urllib.urlopen(url)

    print(f'Connected to {url} successfully')
    print(f'The response code was {response.getcode()}')


if __name__ == '__main__':
    main()