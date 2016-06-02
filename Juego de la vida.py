import pygame
from random import randint
from itertools import permutations

#Se definen los colores
Blanco =  (255, 255, 255)
Verde =  (120, 230, 165)
sc    =  (120, 194, 230)

class JuegodelaVida:
    def __init__(self,rows=10,cols=10):
        self.Cols = cols
        self.Rows = rows
        self.grid = []
        for x in range(self.Rows):
            self.grid.append([])
            for y in range(self.Cols):
                self.grid[x].append(randint(0, 1))
        self.grid2 = self.grid

    def Vecinos(self,xi,yi):
        rango_Vecinos = list(set(permutations([-1,-1,1,1,0],2)))

        outside = lambda x,y: not (x in range(self.Rows) and y in range(self.Cols))
        Vecinos = 0.0
        for range_x, range_y in rango_Vecinos:
            if not outside(xi+range_x, yi+range_y):
                Vecinos += 1 if self.grid[xi + range_x][yi + range_y] else 0
        return Vecinos

    def Roaming(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                vec = self.Vecinos(row,col)

                if(vec < 2  or vec >3):
                    self.grid2[row][col] = 0
                elif (vec == 3):
                    self.grid2[row][col] = 1
        self.grid = self.grid2



m = JuegodelaVida(20,20)


width  = 20
hight = 20
margin = 5

# Inicia  pygame
pygame.init()
DIM_windows = [ (width+margin)*m.Cols + margin , (hight+margin)*m.Rows +  margin ]
Screen = pygame.display.set_mode(DIM_windows)
Screen.fill(sc )

pygame.display.set_caption("Juego de la Vida ")
Finish = False

clock = pygame.time.Clock()


while not Finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finish = True

    
    for row in range(m.Rows):
        for col in range(m.Cols):
            color = Green if(m.grid2[row][col]==1) else White

            pygame.draw.rect(Screen,
                             color,
                             [(margin+width) * col + margin,
                              (margin+hight) * row + margin,
                              width,
                              hight])

    clock.tick(5)

    pygame.display.flip()
    m.Roaming()

pygame.quit()