import json
import time
import random
from tkinter import *

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))

n = 3
m = 0
for x in range(n):
    i = random.randint(0, len(quiz) - 1)
    question = quiz[i]["question"]
            #}\n(1): {quiz[i]["1"]}\n(2): {quiz[i]["2"]}\n(3): {quiz[i]["3"]}\n(4): {quiz[i]["4"]}')
    answer = input('Answer: ')
    if answer == quiz[i]['answer']:
        print('Correct')
        m += 1
    else:
        print('Incorrect')
    time.sleep(1)

label = Label(
    top_frame,
    bg='red',
    fg='green',
    text='question',
    width=12,
    height=4,
    )
