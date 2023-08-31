import random

user_points = 0
computer_points = 0

def main():
    decide()


def decide():
    options = ['rock','paper','scissor']
    while True:
        user_input = input('Your Option: ')
        computer_input = random.choice(options)
        if user_input == 'exit':
            print('Game Ended')
            break
        
        match user_input, computer_input:
            case 'rock', 'rock': print('tie\n')
            case 'paper', 'paper':  print('tie\n')
            case 'scissor', 'scissor':  print('tie\n')
            case 'rock', 'scissor': win('rock', 'scissor','user')
            case 'rock', 'paper': win('rock', 'paper','computer')
            case 'paper', 'rock': win('paper', 'rock','user')
            case 'paper', 'scissor': win('paper', 'scissor','computer')
            case 'scissor', 'paper': win('scissor', 'paper','user')
            case 'scissor', 'rock': win('scissor', 'rock','computer')
            case _: print('no match!'); break

def win(user_input, computer_input, who):
    global user_points
    global computer_points
    print(f'Your Input: {user_input}')
    print(f'Computer Input: {computer_input}')
    if who == 'user':
        user_points += 1
        print('You Win!\n')
    else:
        computer_points += 1
        print('Computer Win!\n')
    print('Score: \n')
    print(f'Your Score: {user_points}')
    print(f'Computer Score: {computer_points}')



if __name__ == '__main__':
    main()