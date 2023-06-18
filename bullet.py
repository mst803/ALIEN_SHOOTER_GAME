import pygame
screen=pygame.display.set_mode((800,600))

#Bullets
class Bullet:
    def __init__(self):
        self.BulletImg=pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\b1.png")
        self.BulletX=0
        self.BulletY=500
        self.BulletX_change=0
        self.BulletY_change=3
        self.Bullet_mode="ready"

    def fire(self,x,y):
        self.Bullet_mode="fire"
        screen.blit(self.BulletImg,(x,y))

    def bullet_move(self):
    #Bullet Movement
        if self.BulletY<=0:
            self.Bullet_mode='ready'
            self.BulletY=500
        if self.Bullet_mode=='fire':
            self.fire(self.BulletX,self.BulletY)
            self.BulletY-=self.BulletY_change

b=Bullet()