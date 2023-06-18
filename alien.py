import pygame
import random
from bullet import b
from settings import s,explotion_sound,explotion_sound2
from game_functions import show,is_collide

screen=pygame.display.set_mode((800,600))

#Enemy
class Alien:
    def __init__(self):
        self.EnemyImg=[]
        self.EnemyX=[]
        self.EnemyY=[]
        self.EnemyX_change=[]
        self.EnemyY_change=[]

        for i in range(s.num_of_Enemy):
            self.EnemyImg.append(pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\alien.png"))
            self.EnemyX.append(random.randint(0,750))
            self.EnemyY.append(40)
            self.EnemyX_change.append(1)
            self.EnemyY_change.append(30)
        
    def Enemy(self,x,y,i):
        screen.blit(self.EnemyImg[i],(x,y))

    def Enemy_move(self):
        #Enemy movement
        for i in range(s.num_of_Enemy):

            if self.EnemyY[i]>450:
                if s.no_of_life > 1:
                    s.no_of_life-=1
                    self.EnemyX[i]=random.randint(0,750)
                    self.EnemyY[i]=40
            
                else:
                    s.no_of_life-=1
                    for j in range(s.num_of_Enemy):
                        self.EnemyY[j]=3000
                    s.game_over=True
                    show.game_over_text()
                    show.game_restart_text()
                    show.Show_fscore(280,360)
                    if s.game_restart:
                        for k in range(s.num_of_Enemy):
                            self.EnemyX[k]=random.randint(0,750)
                            self.EnemyY[k]=40
                        s.game_restart=False
                        s.no_of_life=3
                        s.score_value=0

                    break

            self.EnemyX[i]+=self.EnemyX_change[i]
            if self.EnemyX[i]<=1:
                if s.score_value<10:
                    self.EnemyX_change[i]=1
                elif s.score_value<20:
                    self.EnemyX_change[i]=1.5
                    b.BulletY_change=3.5
                elif s.score_value<30:
                    self.EnemyX_change[i]=2
                    b.BulletY_change=4
                elif s.score_value<40:
                    b.BulletY_change=4.5
                    self.EnemyX_change[i]=2.5
                elif s.score_value<50:
                    b.BulletY_change=5
                    self.EnemyX_change[i]=3
                else:
                    self.EnemyX_change[i]=3.5
                self.EnemyY[i]+=self.EnemyY_change[i]
            elif 750<self.EnemyX[i]:
                if s.score_value<10:
                    self.EnemyX_change[i]=-1
                elif s.score_value<20:
                    self.EnemyX_change[i]=-1.5
                elif s.score_value<30:
                    self.EnemyX_change[i]=-2
                elif s.score_value<40:
                    self.EnemyX_change[i]=-2.5
                elif s.score_value<50:
                    self.EnemyX_change[i]=-3
                else:
                    self.EnemyX_change[i]=-3.5
                self.EnemyY[i]+=self.EnemyY_change[i]
            

            #collition check

            if is_collide(b.BulletX,b.BulletY,self.EnemyX[i],self.EnemyY[i]):
                explotion_sound.play()
                explotion_sound2.play()
                b.BulletY=500
                b.Bullet_mode='ready'
                s.score_value+=1
                self.EnemyX[i]=random.randint(0,750)
                self.EnemyY[i]=40

            self.Enemy(self.EnemyX[i],self.EnemyY[i],i)
enemy = Alien()