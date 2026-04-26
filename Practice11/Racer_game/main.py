#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

 

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("images/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = random.randint(40, SCREEN_WIDTH-40)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path =  ["images/Coin.png","images/Silver.png"]
        orig_image = pygame.image.load(path[0]).convert_alpha()
        self.image = pygame.transform.scale(orig_image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_WIDTH - 40))
    def move(self):
        pass
    def generate(self):
         weight = ["Gold","Silver","Cookie","Bitcoin"]
         rand = random.choice(weight)
         if rand == "Gold":
            orig_image = pygame.image.load("images/Coin.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 1
         elif rand == "Silver":
            orig_image = pygame.image.load("images/Silver.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 2
         elif rand == "Cookie":
            orig_image = pygame.image.load("images/cookie.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 5
         elif rand == "Bitcoin":
            orig_image = pygame.image.load("images/Bitcoin.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 10
            
         return self.value





#Setting up Sprites        
P1 = Player()
E1 = Enemy() 
E2 = Enemy()
newcoin = Coin()
oldcoin = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coin_group = pygame.sprite.Group()
coin_group.add(newcoin)
all_sprites.add(newcoin)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        #if event.type == INC_SPEED:
              #SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                print("added 5 coins!")
                COINS+=5
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coins = font_small.render(f"Coins:{str(COINS)}", True, RED)
    DISPLAYSURF.blit(coins,(310,10))
    speed = font_small.render(f"speed:{str(SPEED)}", True, RED)
    DISPLAYSURF.blit(speed,(300,30))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('sound/crash.wav').play()
          time.sleep(0.5)
          game_over1 = font_small.render(f"Coins collected:{COINS}", True, BLACK)


          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          DISPLAYSURF.blit(game_over1, (120,330))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  

    #Coins collision
    if pygame.sprite.spritecollideany(P1, coin_group):
     coin_value = newcoin.generate()
     COINS += coin_value
     newcoin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 520)
     N = 30
     dc = COINS // N
     SPEED+= dc*0.5
         

   


         
    pygame.display.update()
    FramePerSec.tick(FPS)
