import time
import pygame
import numpy as np

color_bg = (10,10,10)
color_grid = (40,40,40)
color_dead = (170,170,170)
color_alive = (255,255,255)

pygame.init()
pygame.display.set_caption("meow") #or "Game of life"

def update_screen(screen,cells,size,with_progress = False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))

    for row, col in np.ndindex(cells.shape):

        alive = np.sum(cells[row-1:row+2, col-1:col+2])-cells[row,col]
        color = color_bg if cells[row, col] == 0 else color_alive

        if cells[row,col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_dead
            elif 2 <= alive <= 3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = color_alive
        else:
            if alive == 3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = color_alive

        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1)) 

    return updated_cells

def main():

    pygame.init()
    screen = pygame.display.set_mode((800,600))

    cells = np.zeros((60,80))

    screen.fill(color_grid)
    update_screen(screen,cells,10)

    pygame.display.flip()

    running = False

    while True: #main game loop.
        for press in pygame.event.get():
            if press.type == pygame.QUIT:
                pygame.quit()
                return 
            else:
                if press.type == pygame.KEYDOWN:
                    if press.key == pygame.K_SPACE:
                        running = not running
                        update_screen(screen,cells,10)
                        pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10, pos[0]//10] = 1 #this line lits up the pressed position.
                update_screen(screen,cells,10)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update_screen(screen, cells, 10,with_progress=True) #this line update cells with the return value from update_screen.
            pygame.display.update()

        time.sleep(0.001) #delays popping up.
    
if __name__ == "__main__":
    main()


