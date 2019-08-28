from random import randint
import pygame
from parameters import *
from World import *

from Snake import *

world = World(60)
speed = 50
pygame.init()
pygame.display.set_caption("Self-Driving Snake(s)")
SCREEN = pygame.display.set_mode((world.size*SCALE, world.size*SCALE))
CLOCK = pygame.time.Clock()

def dot(location,color):
    pygame.draw.rect(SCREEN, color, (location[0]*SCALE, location[1]*SCALE,SCALE,SCALE))

def repaint(screen, world):
    screen.fill(C_WORLD)

    for i in world.foods:
        dot(i, C_FOOD)

    for i in world.lives:
        # randomColor = (randint(0,255),randint(0,255),randint(0,255))
        for j in i.locations:
            dot(j, C_LIFE)
            # dot(j,randomColor)
    
    pygame.display.flip()


world.addFood();

"""
snake1 = Snake(world,len(world.lives))
world.addLife(snake1)

snake2 = Snake(world,len(world.lives))
world.addLife(snake2)
"""


snakes = [];

for i in range(1):
    newSnake = Snake(world,len(world.lives))
    snakes.append(newSnake)
    world.addLife(newSnake)

stage = 1


while stage == 1:
    repaint(SCREEN, world)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage = 2
        

        # Use these when human wants to play.
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT and snake.direction != LEFT:
        #         snake.changeDirection(RIGHT)
        #     elif event.key == pygame.K_DOWN and snake.direction != UP:
        #         snake.changeDirection(DOWN)
        #     elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
        #         snake.changeDirection(LEFT)
        #     elif event.key == pygame.K_UP and snake.direction != DOWN:
        #         snake.changeDirection(UP)
        #     else:
        #         pass

        #     break

    for i in snakes:
        i.move()

    CLOCK.tick(speed)

    if len(world.lives) == 0:
        stage = 2

SCREEN.fill(BLACK)
pygame.display.flip()
pygame.time.delay(3000)

pygame.quit()