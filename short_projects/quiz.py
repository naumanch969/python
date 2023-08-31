quiz = {
    'one':{
        'question':'What is the capital of Spain?',
        'answer':'Madrid'
    },
    'two':{
        'question':'What is the capital of France?',
        'answer':'Paris'
    },
    'three':{
        'question':'What is the capital of UK?',
        'answer':'London'
    },
    'four':{
        'question':'What is the capital of Germany?',
        'answer':'Berlin'
    },
    'five':{
        'question':'What is the capital of USA?',
        'answer':'Washington'
    },
    'six':{
        'question':'What is the capital of Italy?',
        'answer':'Rome'
    },
    'seven':{
        'question':'What is the capital of Norway?',
        'answer':'Oslo'
    },
    'eight':{
        'question':'What is the capital of Sweden?',
        'answer':'Stockholm'
    },
    'nine':{
        'question':'What is the capital of Portugal?',
        'answer':'Lisbon'
    },
    'ten':{
        'question':'What is the capital of Switzerland?',
        'answer':'Bern'
    },
    'eleven':{
        'question':'What is the capital of Austria?',
        'answer':'Vienna'
    },
    'twelve':{
        'question':'What is the capital of Russia?',
        'answer':'Moscow'
    },
}


score = 5

for key,value in quiz.items():
    print(f'Question: {value["question"]} ')
    answer = input('Answer: ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 5
        print(f'Your score is {score}\n\n')
    else:
        print('Wrong')
        print(f'The answer is {value["answer"]}\n\n')


print(f"You got {score} out of 65 ")
print(f"your percentage is {int(score)/65 * 100 }")