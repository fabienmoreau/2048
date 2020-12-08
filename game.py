
from interface import InterfacePy
import numpy as np
import random
import pygame

class Game:
    def __init__(self, width):
        self.width = width
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.last_state=[]
        self.last_state.append(self.grid)
        self.score = 0
        self.new_element = (0,0)
        self.new_number()

    def get_score(self):
        score=0
        for i in range(self.width):
            for j in range(self.width):
                score+=self.grid[i][j]

    def new_number(self):
        #probability of a 4 is 25%
        list_numbers = [2,2,2,4]
        number = random.choice(list_numbers)
        while True:
            row = int(random.randint(0,self.width-1))
            column = int(random.randint(0,self.width-1))
            if self.grid[row][column]==0:
                self.grid[row][column]=number
                self.new_element = (row,column)
                break

    def slide_left(self):
        move=False
        for row in self.grid:
            for j in range(0,len(row)-1):
                if row[j]==row[j+1] and row[j]!=0:
                    move=True
                    row[j]*=2
                    row[j+1]=0

        for i in range(len(self.grid)):
            new_row=[]
            for number in self.grid[i]:
                if number!=0:
                    new_row.append(number)
            while True:
                if len(new_row)==len(self.grid):
                    break
                else:
                    new_row.append(0)
            if self.grid[i]!=new_row:
                move=True
                self.grid[i]=new_row
                 
        if move == True:
            return True

    def slide_right(self):
        move=False
        for row in self.grid:
            for j in range(0,len(row)-1):
                if row[j]==row[j+1] and row[j]!=0:
                    move=True
                    row[j+1]*=2
                    row[j]=0

        for i in range(len(self.grid)):
            new_row=[]
            for number in self.grid[i]:
                if number!=0:
                    new_row.append(number)
            while True:
                if len(new_row)==len(self.grid):
                    break
                else:
                    new_row.insert(0,0)
            if self.grid[i]!=new_row:
                move=True
                self.grid[i]=new_row
                 
        if move == True:
            return True

    def slide_up(self):
        grid_transposed = list(map(list, zip(*self.grid)))
        move=False
        for row in grid_transposed:
            for j in range(0,len(row)-1):
                if row[j]==row[j+1] and row[j]!=0:
                    move=True
                    row[j]*=2
                    row[j+1]=0

        for i in range(len(grid_transposed)):
            new_row=[]
            for number in grid_transposed[i]:
                if number!=0:
                    new_row.append(number)
            while True:
                if len(new_row)==len(grid_transposed):
                    break
                else:
                    new_row.append(0)
            if grid_transposed[i]!=new_row:
                move=True
                grid_transposed[i]=new_row
                 
        self.grid = list(map(list, zip(*grid_transposed)))

        if move == True:
            return True

    def slide_down(self):
        grid_transposed = list(map(list, zip(*self.grid)))
        move=False
        for row in grid_transposed:
            for j in range(0,len(row)-1):
                if row[j]==row[j+1] and row[j]!=0:
                    move=True
                    row[j+1]*=2
                    row[j]=0

        for i in range(len(grid_transposed)):
            new_row=[]
            for number in grid_transposed[i]:
                if number!=0:
                    new_row.append(number)
            while True:
                if len(new_row)==len(grid_transposed):
                    break
                else:
                    new_row.insert(0,0)
            if grid_transposed[i]!=new_row:
                move=True
                grid_transposed[i]=new_row         
        
        self.grid = list(map(list, zip(*grid_transposed)))

        if move == True:
            return True 




if __name__=='__main__':
    game=Game(4)
    interface=InterfacePy()
    while True:
        interface.refresh(game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if game.slide_left()==True:
                        game.new_number()
                        game.last_state.append(game.grid)
                elif event.key == pygame.K_RIGHT:
                    if game.slide_right()==True:
                        game.new_number()
                        game.last_state.append(game.grid)
                elif event.key == pygame.K_UP:
                    if game.slide_up()==True:
                        game.new_number()
                        game.last_state.append(game.grid)
                elif event.key == pygame.K_DOWN:
                    if game.slide_down()==True:
                        game.new_number()
                        game.last_state.append(game.grid)
                elif event.key == pygame.K_w:
                    print(game.last_state)
                    if game.last_state[-1]==game.grid:
                        game.last_state.pop()
                        game.grid=game.last_state.pop()
                    else:
                        game.grid=game.last_state.pop()
                    print(game.last_state)