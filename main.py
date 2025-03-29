from turtle import screensize, speed, width
import pygame, random, json, sys

"""
Important:
    Mechanics
    Images
    BGM
"""

# Save Data

player_Data = {
    "username" : "",
    "health" : "100",
    "level" : "1",
    "exp" : "0"
}

pygame.init()
"""
    Setting:
    Graphics
    Sounds
"""
WIDTH = 500
HEIGHT = 480
FPS = 60

frames = pygame.time.Clock()
Screen = pygame.display.set_mode((HEIGHT, WIDTH))
get_screen_size = Screen.get_rect()

"""
    Set up of character
    character animation
"""
char_width, char_height = 50, 50
char_x, char_y = char_width / 2, char_height / 2
char_speed = [5, 5]

char_walk_frames = [
    pygame.image.load("./bg/char/frame1.png").convert_alpha(),
    pygame.image.load("./bg/char/frame2.png").convert_alpha(),
    #pygame.image.load("./bg/char/frame3.png").convert_alpha()
]; frames_index = 0


menuBGM = pygame.mixer_music.load("./bgm/audio.mp3")
pygame.mixer_music.play((999))

while True:
    print(char_x, char_y)

#Check If user is quitting
    for ev in pygame.event.get():
        #print(ev)
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    """
        Controls
        Screen Collision
    """
    Keys  = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        char_y -= char_speed[1]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_y < 0:
            char_y = -char_speed[0]
    elif Keys[pygame.K_s]:
        char_y += char_speed[1]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_y > WIDTH:
            char_y -= char_speed[1]
    elif Keys[pygame.K_a]:
        char_x -= char_speed[0]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_x < 0:
            char_x = -char_speed[0]
    elif Keys[pygame.K_d]:
        char_x += char_speed[0]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_x > WIDTH:
            char_x -= char_speed[0]
    """
        Update content
        Refresh Rate
    """
    Screen.fill(("#255c14"))
    Screen.blit(char_walk_frames[frames_index], (char_x, char_y))
    pygame.display.flip()
    frames.tick(FPS)
