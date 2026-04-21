import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_small = pygame.font.SysFont("Verdana", 20)
CELL = 30

COUNTER = 0

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1


    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global COUNTER
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            COUNTER += 1
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self.body)

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self,snake_body):
        while True:
            # 1. Generate a potential location
            newx = random.randint(0, WIDTH // CELL - 1)
            newy = random.randint(0, HEIGHT // CELL - 1)
            
            # 2. Check if this location overlaps with ANY part of the snake
            overlapping = False
            for segment in snake.body:
                if segment.x == newx and segment.y == newy:
                    overlapping = True
                    break
            
            # 3. If no overlap, set the position and exit the loop
            if not overlapping:
                self.pos.x = newx
                self.pos.y = newy
                break


FPS = 5
clock = pygame.time.Clock() 
food = Food()
snake = Snake()


running = True
while running:

    scores = font_small.render(str(COUNTER), True, colorRED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    screen.fill(colorBLACK)



    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

'''
#
# # #

-----

#
#
# #

-----

#
#
#
#

'''