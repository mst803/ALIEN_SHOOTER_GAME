import pygame
from ship import p
from bullet import b
from settings import *
from game_functions import show
from alien import enemy


pygame.init()

#game window
screen=pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Alien shooter 2")
icon=pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\icon.jpg")
pygame.display.set_icon(icon)

#background
background=pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\bg.png")


running=True
while running:

    screen.fill((120,230,250))
    screen.blit(background,(0,0))
    heart()

    
    for i in pygame.event.get():

        if i.type==pygame.QUIT:
            running=False
        
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                p.playerX_change=-3
            if i.key==pygame.K_RIGHT:
                p.playerX_change=3

            if i.key==pygame.K_KP_ENTER:
                s.game_starting=False
                if s.game_over:
                    s.game_restart=True

            if i.key==pygame.K_SPACE:
                if b.Bullet_mode=='ready' and not s.game_starting:
                    bullet_sound.play()
                    b.BulletX=p.playerX-12
                    b.fire(b.BulletX,b.BulletY)
                
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT:
                p.playerX_change=0

    if s.game_starting:
        show.game_start_text("GET READY")

    else:
        p.player_move()
        b.bullet_move()
        enemy.Enemy_move()

    show.show_score(10,10)
    pygame.display.update()