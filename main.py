import pygame, json

"""
Important:
    Mechanics
    Images
    BGM
"""

pygame.init()
frames = pygame.time.Clock()
surface = pygame.display.set_mode((600, 500))
surfRect = surface.get_rect()

menuBG = pygame.image.load("./bg/photo.jpg")


menuBGM = pygame.mixer_music.load("./bgm/audio.mp3")
pygame.mixer_music.play()

while True:
    for ev in pygame.event.get():
        print(ev)
        if ev.type == pygame.QUIT:
            pygame.quit()
    frames.tick(60)
    surface.blit(menuBG, surfRect)
    pygame.display.flip()
