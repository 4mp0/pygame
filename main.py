import pygame, json, sys

from pygame.constants import KEYDOWN

"""
Important:
    Mechanics
    Images
    BGM
"""

player_Data = {
    "username" : "",
    "level" : ""
}

pygame.init()

frames = pygame.time.Clock()
Scrreen = pygame.display.set_mode((600, 500))
surfRect = Scrreen.get_rect()

char = pygame.Rect((0, 0), (128, 128))

menuBG = pygame.image.load("./bg/photo.jpg")

menuBGM = pygame.mixer_music.load("./bgm/audio.mp3")
pygame.mixer_music.play((999))

while True:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Keys  = pygame.key.get_pressed()

    if Keys[pygame.K_w]:
        char.y -= 5
    elif Keys[pygame.K_s]:
        char.y += 5
    elif Keys[pygame.K_a]:
        char.x -= 5
    elif Keys[pygame.K_d]:
        char.x += 5

    frames.tick(60)
    Scrreen.blit(menuBG, surfRect)
    #Scrreen.fill((0, 0, 0))
    pygame.draw.rect(Scrreen, (255, 255, 255), char)
    pygame.display.flip()
