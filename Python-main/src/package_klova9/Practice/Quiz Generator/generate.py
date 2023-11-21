import json
import random

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))

i = random.randint(0, len(quiz) - 1)
print(f'Question: {quiz[i]["question"]}\n(1): {quiz[i]["1"]}\n(2): {quiz[i]["2"]}\n(3): {quiz[i]["3"]}\n(4): {quiz[i]["4"]}')
answer = input('Answer: ')
if answer == quiz[i]['answer']:
    print('Correct')
else:
    print('Incorrect')