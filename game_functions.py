import pygame
from settings import s
import numpy as np

screen=pygame.display.set_mode((800,600))


#game functions

class Fonts:
    font=pygame.font.Font(r'C:\Users\shahi\Desktop\GAME\resourses\Boba Cups.ttf',32)
    game_over_font=pygame.font.Font(r"C:\Users\shahi\Desktop\GAME\resourses\Best Love DEMO.ttf",100)
    game_start_font=pygame.font.Font(r"C:\Users\shahi\Desktop\GAME\resourses\Best Love DEMO.ttf",70)
    info_font=pygame.font.Font(r"C:\Users\shahi\Desktop\GAME\resourses\Philosopher-Regular.ttf",30)
    
    
    def show_score(self,x,y):
        self.score=self.font.render("Score: "+str(s.score_value),True,(255,255,255))
        screen.blit(self.score,(x,y))

    def Show_fscore(self,x,y):
        self.score=self.font.render("Your Score: "+str(s.score_value),True,(255,255,255))
        screen.blit(self.score,(x,y))

    def game_over_text(self):
        self.game_over=self.game_over_font.render("GAME OVER",True,(255,50,50))
        screen.blit(self.game_over,(150,200))

    def game_start_text(self,i):
        self.game_start=self.game_start_font.render(i,True,(25,255,25))
        self.start_info=self.info_font.render("Press Enter to start",True,(255,255,255))
        screen.blit(self.game_start,(235,235))
        screen.blit(self.start_info,(275,320))

    def game_restart_text(self):
        self.restart_info=self.info_font.render("Press Enter to Restart",True,(255,255,255))
        screen.blit(self.restart_info,(255,450))
    
#collition
def is_collide(BulletX,BulletY,EnemyX,EnemyY):
    distance=np.sqrt((BulletX-(EnemyX-20))**2+(BulletY-EnemyY)**2)
    if distance<20:
        return True
    else:
        return False

show=Fonts()
