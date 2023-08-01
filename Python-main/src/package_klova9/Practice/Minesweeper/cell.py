from tkinter import *
import random
import main
from PIL import Image, ImageTk
import settings

class Cell:
    all = []
    def __init__(self, x, y,  is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x = x
        self.y = y
        Cell.all.append(self)
        
    def create_cell_button(self, location):
        img = Image.open('Python-main\src\package_klova9\Practice\Minesweeper\grass.png')
        canvas = Canvas(main.root, width = 1, height = 1)
        ph = ImageTk.PhotoImage(master = canvas, image = img)
        btn = Button(
        location,
        image=ph,
        relief='raised',
        borderwidth=4,
        text = f'{self.x}, {self.y}',
        padx=11,
        pady=11,
        )
        btn.bind('<Button-1>', self.l_click)
        btn.bind('<Button-3>', self.r_click)
        self.cell_button = btn
        
    def l_click(self, event):
        
        if self.is_mine:
            self.show_mine
        else:
            self.show_cell()
    
    def r_click(self, event):
        print('RClick')
        
         
    def get_cell(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        
    def show_cell(self):
        self.cell_button.configure(relief = 'sunken')
      
    def show_mine(self):
        self.cell_button.configure(bg= 'red') 
    
    
    @staticmethod
    def randomize_mines():
        mined = random.sample(Cell.all, settings.MINE_COUNT)
        for mine in mined:
            mine.is_mine = True
            print(f'Mine at {mine}')
    
    
    def __repr__(self):
        return(f'{self.x}, {self.y}')