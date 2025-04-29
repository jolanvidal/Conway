import pygame as py

import numpy as np

# GLOBAL VARIABLES
WIDTH, HEIGHT = 900,900
blockSize = 30
list_of_lists = [[False]*int(WIDTH / blockSize)]*int(HEIGHT / blockSize)
board = np.array(list_of_lists)

# Colors
black = (0,0,0)
white = (255,255,255)
dark = (100,100,100)
red = (255,0,0)

py.init()
py.font.init()

fps = 60

font = py.font.Font('freesansbold.ttf', 32)

clock = py.time.Clock()

screen = py.display.set_mode((WIDTH, HEIGHT))

py.display.set_caption('Game of life')

def main():
    global fps
    isRunning = True
  
    while isRunning:          
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.MOUSEBUTTONDOWN:
                click()  
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    isRunning = False;     
                if event.key == py.K_DOWN:
                    if fps <= 1:
                        fps = 1
                    else:
                        fps = fps - 1
                    print("DOWN")
                if event.key == py.K_UP:
                    if fps >= 60:
                        fps = 60
                    else:
                        fps = fps + 1   
                    print("UP")
        selectBlock()
        draw_fps()
        py.display.flip()
        clock.tick(fps)   



    print("Out of loop")  
    isRunning = True
    while isRunning:
        clock.tick(fps)        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()           
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    isRunning = False;        
        play()

def getFpsText():
    return font.render(str(fps), True, red, black)

def play():
    print("Go")

def draw_board():
    for x in range(int(WIDTH / blockSize)):
        for y in range(int(HEIGHT / blockSize)):
            rect = py.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            py.draw.rect(screen, white, rect, 1) 

    for x in range(int(WIDTH / blockSize)):      
        for y in range(int(HEIGHT / blockSize)):
            if (board[x,y] == True):
                py.draw.rect(screen, white, (x * blockSize, y * blockSize, blockSize, blockSize))
   
def draw_fps():
    rect = py.Rect(0,0,20,20)
    screen.blit(getFpsText(), rect )   
    

def selectBlock():
    screen.fill(black)
    draw_board()
    

def click():
    mX, mY = py.mouse.get_pos()
    x = int(mX/blockSize)
    y = int(mY/blockSize)
    print(x, y)
    if (board[x,y] == True):
        board[x,y] = False
    else:
        board[x,y] = True

main()
   