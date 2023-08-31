import os

if __name__ == '__main__':
    while True:
        x = input('Enter what you want to pronounce: ')
        if x == 'q':
            os.system('espeak "bye bye friends"')
            break
        command = f'espeak "{x}"'
        os.system(command)