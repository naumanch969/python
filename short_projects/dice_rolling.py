import random

def main():
    roll_dice()

def roll_dice():
    roll = input('Roll the dice? (Y/N) ')
    while roll.lower() == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'roll 1: {dice1}')
        print(f'roll 2: {dice2}')
        roll = input('Roll again? (Y/N) ')


if __name__ == '__main__':
    main()