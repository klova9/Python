import json
import time
import random
from tkinter import *

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))
root = Tk()
HEIGHT = 300
WIDTH = 300
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title("Pop Quiz")
root.resizable(False, False)
root.pack_propagate(False)

top_frame = Frame(
    root,
    width=WIDTH,
    height=HEIGHT * 0.25
    )
top_frame.place(x=0, y=0)
center_frame = Frame(
    root,
    bg='black',
    width= WIDTH,
    height=HEIGHT * 0.75
)

center_frame.place(x=0, y=HEIGHT * 0.25)
def generate():
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
    return question
        
label = Label(
    top_frame,
    bg='red',
    fg='green',
    text=generate(),
    width=12,
    height=4,
    )
label.pack()
root.update()
root.mainloop()