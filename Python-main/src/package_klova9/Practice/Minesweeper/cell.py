from tkinter import *
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count_label = None
    cell_count = settings.CELL_COUNT
    print(f'Cell count: {cell_count}')
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.cell_btn_object = None
        self.isMarked = False
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=6,
            height=2,
            relief='raised',
            borderwidth=8
        )
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click=
        self.cell_btn_object = btn
        
           
    
    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            text=f'Tiles left:  {Cell.cell_count - settings.MINES_COUNT}', font='gostcom 16 bold',
            width=12,
            height=4,
            bg='black',
            fg='red'
        )
     
        Cell.cell_count_label = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
               for cell_obj in self.surrounded_cells:
                   cell_obj.show_cell() 
            self.show_cell()
        self.cell_btn_object.config(relief='sunken')
        return 'break'
            
    def right_click_actions(self, event):
        if not self.isMarked and not  self.is_open:
            self.cell_btn_object.config(bg='orange')
            self.isMarked = True
        else:
            self.cell_btn_object.config(bg='SystemButtonFace')
            self.isMarked = False
    def get_cell_by_axis(self, x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        i = {
            0: 'green',
            1: 'blue',
            2: 'yellow',
            3: 'orange',
            4: 'red',
            5: 'brown'
        }
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        for k, v in i.items():
            if k == counter:
                self.cell_btn_object.configure(fg=v)
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length, font='ComicSansMS 10', relief='sunken', bg='SystemButtonFace')
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text=f'Tiles left:  {Cell.cell_count - settings.MINES_COUNT}')
        self.is_open = True
        if self.surrounded_cells_mines_length == 0:
            for cell_obj in self.surrounded_cells:
                cell_obj.show_cell()
        
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
       # ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
       # sys.exit()
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        print(settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"