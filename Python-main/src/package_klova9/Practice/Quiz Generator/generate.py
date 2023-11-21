import json
import time
import random

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))
n = 3
m = 0
for x in range(n):
    i = random.randint(0, len(quiz) - 1)
    print(f'Question: {quiz[i]["question"]}\n(1): {quiz[i]["1"]}\n(2): {quiz[i]["2"]}\n(3): {quiz[i]["3"]}\n(4): {quiz[i]["4"]}')
    answer = input('Answer: ')
    if answer == quiz[i]['answer']:
        print('Correct')
        m += 1
    else:
        print('Incorrect')
    time.sleep(1)
    print('\n\n')
print('You got ' + str(m) + ' out of ' + str(n) + ' correct')
    