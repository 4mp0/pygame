import pygame, sys

pygame.init()
pygame.display.set_caption("Omotale")
#pygame.display.set_icon("")

screen_w, screen_h, fps, bgm_vol = 600, 400, 60, 0.05
game_speed = 2, 2


screen = pygame.display.set_mode((screen_w, screen_h))
screen_rect = screen.get_rect()
frames = pygame.time.Clock()

char = [
    pygame.image.load("./bg/char/frame1.png").convert_alpha(),
    pygame.image.load("./bg/char/frame2.png").convert_alpha(),
    pygame.image.load("./bg/char/frame3.png").convert_alpha()
]
rvrs_img_bool = False
char_pos = char.get_rect()
frames_index = 0

while True:
            
    Keys  = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        char_pos.y -= game_speed[1]
    elif Keys[pygame.K_a]:
        char_pos.x -= game_speed[0]
    elif Keys[pygame.K_s]:
        char_pos.y += game_speed[1]
    elif Keys[pygame.K_d]:
        char_pos.x += game_speed[0]

    if not screen_rect.collidepoint(char_pos.x, char_pos.y):
        char_pos.clamp_ip(screen_rect)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(char, (char_pos.x, char_pos.y))

    frames.tick(fps)
    pygame.display.update()
