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

frame = tkinter.Frame(root)
frame.place()
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

label = tkinter.Label(frame, question)
label.place(frame)
root.mainloop()