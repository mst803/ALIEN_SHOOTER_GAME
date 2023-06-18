import pygame
screen=pygame.display.set_mode((800,600))

#player

class Ship:
    def __init__(self):
        self.playerImg=pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\ship.png")
        self.playerX=400
        self.playerY=500
        self.playerX_change=0
    
    def player(self,x,y):
        screen.blit(self.playerImg,(x,y))

    def player_move(self):
        #player movement
        self.playerX+=self.playerX_change
        if self.playerX<0:
            self.playerX=0
        elif self.playerX>760:
            self.playerX=760
        self.player(self.playerX,self.playerY)
    
p=Ship()