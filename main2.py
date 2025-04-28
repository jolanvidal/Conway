import pygame as py;

import numpy as np

# GLOBAL VARIABLES
WIDTH, HEIGHT = 900,900
blockSize = 30
list_of_lists = [[0]*blockSize]*blockSize
board = np.array(list_of_lists)

# Colors
black = (0,0,0)
white = (255,255,255)
dark = (100,100,100)

fps = 3

py.init()

clock = py.time.Clock()

screen = py.display.set_mode((WIDTH, HEIGHT))

py.display.set_caption('Game of life')

def draw_grid():
    for i in range(WIDTH / blockSize):
       pg.draw.line(screen, white)
    

def draw_grid():
    for i in range(row):
        pg.draw.line(screen, white, (0, i * row), (row * row, i * col), 1)
        pg.draw.line(screen, white, (i * col, 0), (i * row,col * col), 1)

def selectBlock():
    screen.fill(black)
    draw_grid()    
    draw_cells()
    draw_button()
    pg.display.update()

def click():
    mX, mY = py.mouse.get_pos()
    print(mX, mY)

def main():
    isRunning = True
    while isRunning:        
        clock.tick(fps)        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                click()            
            if event.key == py.K_SPACE:
                isRunning = False
    print("Out of loop")       
   