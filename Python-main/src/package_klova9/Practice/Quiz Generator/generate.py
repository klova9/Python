import json
import time
import random
import tkinter

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))
root = tkinter.Tk()
root.geometry("300x300")
root.title("Pop Quiz")
root.resizable(False, False)
root.pack_propagate(False)

top_frame = tkinter.Frame(
    root,
    width=300,
    height=50,)
top_frame.place(x=0, y=0)
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
    print('\n')

label = tkinter.Label(
    top_frame,
    fg='black',
    text=question,
    )
label.place(x=0, y=50)
root.mainloop()