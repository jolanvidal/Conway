import pygame as py

import numpy as np

# GLOBAL VARIABLES
WIDTH, HEIGHT = 900,900
blockSize = 30
list_of_lists = [[0]*int(WIDTH / blockSize)]*int(HEIGHT / blockSize)
board = np.array(list_of_lists)

# Colors
black = (0,0,0)
white = (255,255,255)
dark = (100,100,100)

fps = 60

py.init()

clock = py.time.Clock()

screen = py.display.set_mode((WIDTH, HEIGHT))

py.display.set_caption('Game of life')

def draw_board():
    for x in range(int(WIDTH / blockSize)):
        for y in range(int(HEIGHT / blockSize)):
            rect = py.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            py.draw.rect(screen, white, rect, 1)       

   

def selectBlock():
    screen.fill(black)
    draw_board()
    

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
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    isRunning = False;        
        selectBlock()
        py.display.flip()
    print("Out of loop")       

main()
   