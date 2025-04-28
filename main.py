import pygame as pg
import sys

from pygame.locals import *
import numpy as np
import math

# GLOBAL VARIABLES
colWidth = 30
rowWidth = 30

row = 30
col = 30

# RUNNING
isRunning = True

# BOARD (ONLY USING BOARD)
list_of_lists = [[0]*col]*row
board = np.array(list_of_lists)

# SCREEN SIZE
width = 1000
height = 900

# COLORS
black = (0,0,0)
white = (255,255,255)
dark = (100,100,100)

# FPS
fps = 3


# Pygame
pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))

pg.display.set_caption('Game of life')

def draw_grid():
    for i in range(row):
        pg.draw.line(screen, white, (0, i * row), (row * row, i * col), 1)
        pg.draw.line(screen, white, (i * col, 0), (i * row,col * col), 1)

def draw_cells():
    for x in range(col):
        for y in range(row):
            if (board[x,y] == 1):
                pg.draw.rect(screen, white, (x * col, y * row, colWidth, rowWidth))      
                
def draw_button():
    pg.draw.rect(screen, dark, (925, 100, 50, 20))
        
def init_board():
    screen.fill(black)
    draw_grid()    
    draw_cells()
    draw_button()
    pg.display.update()

def render():
    screen.fill(black)
    draw_grid()    
    draw_cells()
    pg.display.update()
    
def click():     
    mX,mY = pg.mouse.get_pos()
    print("CLICK", mX, mY)
    if (mX < colWidth * col):
        board[int(mX / colWidth), int(mY / rowWidth)]= 1
        return False
    elif (mX >= 925 and mX <= 975):   
        print("CLICK BUTTON")
        return True
    
  
   
    
def updateGame():
    for x in range(col):
        for y in range(row):
            if (x < 1 or y < 1):
                print("SMaller")
    
def main():  
    while isRunning:
        clock.tick(fps)        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if (click()):
                    isRunning = False
        init_board()        
        
    print("END RUNNING")
    # while run:
    #     clock.tick(fps)
    
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()
    #         if event.type == pg.MOUSEBUTTONDOWN:
    #             click()
    #     #updateGame()
    #     render()

        
        
main()
        
        
            
                
            