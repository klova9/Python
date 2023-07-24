from tkinter import *
import settings
from cell import Cell

root = Tk()

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
root.title('Minesweeper')
top_frame = Frame(
    root,
    bg='grey',
    width=settings.WIDTH,
    height=settings.HEIGHT/8,
)
top_frame.place(x=0, y=0)
left_frame = Frame(
    root,
    bg='grey',
    width=settings.WIDTH/8,
    height=settings.HEIGHT,
)
left_frame.place(x=0, y=settings.HEIGHT/8)
center_frame = Frame(
    root,
    bg='blue',
    width=settings.WIDTH*7/8,
    height=settings.HEIGHT*7/8,
)
center_frame.place(x=settings.WIDTH/8, y=settings.HEIGHT/8)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x,y)
        cell.create_cell_button(center_frame)
        cell.cell_button.grid(row=y, column=x)
Cell.randomize_mines()

root.mainloop()
