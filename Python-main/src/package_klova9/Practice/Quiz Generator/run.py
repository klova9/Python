import tkinter
import generate

question = generate()
root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
label = tkinter.Label(frame, question = q)
root.mainloop()