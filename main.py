import pygame, random, json, sys

"""
Important:
    Mechanics
    Images
    BGM
"""

player_Data = {
    "username" : "",
    "health" : "100",
    "level" : "1",
    "exp" : "0"
}

pygame.init()

frames = pygame.time.Clock()
Screen = pygame.display.set_mode((600, 500))
surfRect = Screen.get_rect()

"""
    Set up of character
    Load character animation
    
"""
char_width, char_height = 50,50
char_x, char_y = char_width / 2, char_height / 2
char_speed = 5

char_walk_frames = [
    pygame.image.load("./bg/char/frame1.png").convert(),
    pygame.image.load("./bg/char/frame2.png").convert()
]


frames_index = 0

#menuBG = pygame.image.load("./bg/photo.jpg")
#opp_apprd = pygame.image.load("")

menuBGM = pygame.mixer_music.load("./bgm/audio.mp3")
pygame.mixer_music.play((999))

while True:
#Check If user is quitting
    for ev in pygame.event.get():
        #print(ev)
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#Controls
    Keys  = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        char_y -= char_speed
        frames_index = (frames_index + 1) % len(char_walk_frames)
    elif Keys[pygame.K_s]:
        char_y += char_speed
        frames_index = (frames_index + 1) % len(char_walk_frames)

    elif Keys[pygame.K_a]:
        char_x -= char_speed
        frames_index = (frames_index + 1) % len(char_walk_frames)
    elif Keys[pygame.K_d]:
        char_x += char_speed
        frames_index = (frames_index + 1) % len(char_walk_frames)
        opp_appear_chance = random.randint(0, 100)

    Screen.fill(("#255c14"))

    
    Screen.blit(char_walk_frames[frames_index], (char_x, char_y))

    pygame.display.flip()
    frames.tick(60)
