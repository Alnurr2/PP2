import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_small = pygame.font.SysFont("Verdana", 20)
CELL = 40

COUNTER = 0
font_score = pygame.font.SysFont("Verdana", 18)
score = 0

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
        self.score = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > WIDTH // CELL - 1:
            return False
        # checks the left border
        if self.body[0].x < 0:
            return False
        # checks the bottom border
        if self.body[0].y > HEIGHT // CELL - 1:
            return False
        # checks the top border
        if self.body[0].y < 0:
            pygame.display.update()
            return False
        

        return True
            



    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global COUNTER,time_passed
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print(f"Got food!:+{food.value}")
            COUNTER += food.value
            self.score+=food.value
            self.body.append(Point(head.x, head.y))
            time_passed = pygame.time.get_ticks() - 10000
            food.generate_random_pos(self.body)
            pygame.time.set_timer(FOOD_EVENT, 15000)
        
        if head.x in self.body and head.y in self.body:
            return False 
        return True
    def body_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if segment.x == head.x and segment.y == head.y:
                return True
        return False

snake = Snake()
class Food:
    def __init__(self,snake_body):
        snake = Snake()
        self.pos = Point(9, 9)
        self.color = colorGRAY 
        self.value = 1
        self.generate_random_pos(snake_body)

    def draw(self):
        global color
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


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
        global color
        weight = ["Gold","Silver","Cookie"]
        rand = random.choice(weight)
        if rand == "Gold":
            self.color = colorGREEN
            self.value = 1
        elif rand == "Silver":
            self.color = colorRED
            self.value = 2
        elif rand == "Cookie":
            self.color = colorBLUE
            self.value = 3
        return self.value


FPS = 5
clock = pygame.time.Clock() 
food = Food(snake.body)
snake = Snake()

FOOD_EVENT = pygame.USEREVENT + 1


running = True
while running:

    scores = font_small.render(f"Food:{str(COUNTER)}", True, colorRED)
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
        if event.type == FOOD_EVENT:
            food.generate_random_pos(snake.body)
            

    screen.fill(colorBLACK)
    draw_grid_chess()
    alive = snake.move()


    
    
    if alive:
        running =  True
    else:
        running = False
    

    if snake.body_collision():
        running = False
    else:
        snake.check_collision(food)
    
    food.draw()
    snake.draw()
    image_score = font_score.render(f"Score: {snake.score}", True, colorBLACK)
    image_level = font_score.render(f"Level: {snake.score//4 + 1}", True, colorBLACK)

    image_score_rect = image_score.get_rect(topright = (WIDTH - 10, 10))
    image_level_rect = image_level.get_rect(topright = (WIDTH - 10, 30))
    
    screen.blit(image_score, image_score_rect)
    screen.blit(image_level, image_level_rect)
    FPS = 5 + snake.score//4
    screen.blit(scores,(30,30))

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