import pygame
import math

done = False
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

my_font = pygame.font.SysFont(None, 36)

current_track = 0
musics = ["music/music1.mp3","music/music2.mp3"]
track_info = pygame.mixer.Sound("music/music1.mp3")
for i in range(len(musics)):
       track_len = []
       len = pygame.mixer.Sound(musics[i])
       track_len.append(len)
print(str(track_len))
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_p:
                              pygame.mixer.music.load(musics[current_track])
                              pygame.mixer.music.play()
                              print("Playing!")
                if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_s:
                              pygame.mixer.music.pause()
                              print("On pause!")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        current_track +=1
                        pygame.mixer.music.load(musics[current_track])
                        pygame.mixer.music.play()
                        print("Next!")
                if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_b:
                              current_track -=1
                              pygame.mixer.music.load(musics[current_track])
                              pygame.mixer.music.play()
                if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_q:
                              done = True


        pos_ms = pygame.mixer.music.get_length()
        pos_sec = pos_ms / 1000 if pos_ms != -1 else 0
        total_sec = pos_ms

        #seconds = lenin/60 - math.floor(lenin/60)
        cur = my_font.render(f"Current Track:{musics[current_track]}", True, (0, 0, 0))
        time_text = my_font.render(f"Time: {int(pos_sec)}s / {int(total_sec)}s", True, (0, 0, 0))
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                        pygame.mixer.music.pause()
        if event.type == pygame.K_n:
               if event.key == pygame.K_n:
                      current_track +=1
               pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_b:
                      current_track -=1
        

        screen.fill((255,255,255))
        screen.blit(cur,(10,30))
        screen.blit(time_text,(10,50))
        pygame.display.flip()
        clock.tick(60)




















