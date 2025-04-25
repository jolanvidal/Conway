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
board = []


width = 1000
height = 900

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Pygame
pg.init()

fps = 60

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))

pg.display.set_caption('Game of life')

def init_board():
    array = []
    for i in range(col):
        array.append(False)
    
    for i in range(col):
        board.append(array)    
    

def draw_grid():
    for i in range(row):
        pg.draw.line(screen, white, (0, i * row), (row * row, i * col), 1)
        pg.draw.line(screen, red, (i * col, 0), (i * row,col * col), 1)
        
    for i in range(col):
        for j in range(row):
            if (board[i][j] == True):
                pg.draw.rect(screen, white, (i, j, colWidth, rowWidth))
        
        

def render():
    screen.fill(black)
    draw_grid()    
    
    pg.display.update()
    
def click():
    mX,mY = pg.mouse.get_pos()
    
    if mX <= col * colWidth:
        x = mX / col
        y =mY / row
        board[int(x)][int(y)] = True
        print(int(x), int(y))
    
    
    
def main():    
    init_board()    
        
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                click()
        render()
        
        
main()
        
        
            
                
            