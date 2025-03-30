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
pygame.display.set_caption("Omotale")
#pygame.display.set_icon("")
"""
    Setting:
    Graphics
    Sounds
"""
WIDTH = 500
HEIGHT = 480
FPS = 60
BGM_vol = 0.05

frames = pygame.time.Clock()
Screen = pygame.display.set_mode((HEIGHT, WIDTH))
get_screen_size = Screen.get_rect()

pygame.mixer_music.set_volume(BGM_vol)
"""
    Set up of character
    character animation
"""
char_width, char_height = 50, 50
char_x, char_y = char_width / 2, char_height / 2
char_speed = [5, 5]
rvrs_img_bool = False

char_walk_frames = [
    pygame.image.load("./bg/char/frame1.png").convert_alpha(),
    pygame.image.load("./bg/char/frame2.png").convert_alpha(),
    #pygame.image.load("./bg/char/frame3.png").convert_alpha()
]; frames_index = 0

menu_BGM = [
    #pygame.mixer_music.load("./bgm/audio1.mp3"),
    #pygame.mixer_music.queue(("./bgm/audio2.mp3")),
    #pygame.mixer_music.queue(("./bgm/audio3.mp3"))
]
#pygame.mixer_music.play(len(menu_BGM))

npc1 = pygame.image.load("./bg/npc/frame1.png").convert_alpha()
npc1Pos = npc1.get_rect()
npc1Pos.y = 5
while True:
    print(char_x, char_y)
    """
        Log events incase of bugs
        Check for quit event
    """
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
    """
        Controls
        Screen Collision
    """
    Keys  = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        rvrs_img_bool = False
        char_y -= char_speed[1]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_y < 0:
            char_y = -char_speed[1]
    elif Keys[pygame.K_s]:
        rvrs_img_bool = False
        char_y += char_speed[1]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_y > WIDTH:
            char_y -= char_speed[1]
    elif Keys[pygame.K_a]:
        rvrs_img_bool = False
        char_x -= char_speed[0]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_x < 0:
            char_x = -char_speed[0]
    elif Keys[pygame.K_d]:
        rvrs_img_bool = True
        char_x += char_speed[0]
        frames_index = (frames_index + 1) % len(char_walk_frames)
        if char_x > WIDTH:
            char_x -= char_speed[0]
    """
        Reverse Image upon meeting condition
    """
    img_copy = char_walk_frames[frames_index].copy()
    char_pos = img_copy.get_rect()
    char_pos.x = char_x
    char_pos.y = char_y
    img_rvs = pygame.transform.flip(img_copy, rvrs_img_bool, False)
    
    if char_pos.colliderect(npc1Pos):
        print("Collision has occurred!")
    """
        Update content
    """
    Screen.fill(("#255c14"))
    Screen.blit(npc1, (npc1Pos.x, npc1Pos.y))
    Screen.blit(img_rvs, (char_x, char_y))
    pygame.display.flip()
    frames.tick(FPS)
