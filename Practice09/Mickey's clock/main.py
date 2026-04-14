import pygame
from datetime import datetime

wtime = datetime.now()
print(wtime)
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
my_font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
done = False

PIVOT_X, PIVOT_Y = 485, 335
offset = pygame.math.Vector2(0, 100)

angle = 180
dt = clock.tick(60) / 1000.0
sample_img = pygame.image.load("mickey.png").convert_alpha()
hand1 = pygame.image.load("hand.png").convert_alpha()
smaller_img = pygame.transform.scale(hand1, (200, 200))
hand2 = pygame.image.load("mickey.png").convert_alpha()

image_height = smaller_img.get_height()
hand_length = image_height // 2


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        keys = pygame.key.get_pressed()
        angle-= 50* dt
        
        counter = pygame.time.get_ticks()//1000
        counter1 = counter / 60
        seconds = my_font.render(f"seconds: {counter}s", True, (0, 0, 0))
        minutes = my_font.render(f"minutes: {counter1}", True, (0, 0, 0))

        rotated = pygame.transform.rotate(smaller_img,angle)

        rotated_offset = offset.rotate(-angle)
        rect = rotated.get_rect(center=(PIVOT_X + rotated_offset.x, PIVOT_Y + rotated_offset.y))
        rect1 = rotated.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        center1 = sample_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
       
        screen.fill((255, 255, 255))
        mickey_rect = sample_img.get_rect(center=(WIDTH // 2 + 30, HEIGHT // 2 + 20))
        screen.blit(sample_img,mickey_rect)
        screen.blit(rotated,rect)
        screen.blit(seconds, (10, 10))
        screen.blit(minutes, (10, 30))

        pygame.display.flip()

        clock.tick(60)
        print(counter1)
