import pygame
from pygame import mixer


pygame.init()

screen=pygame.display.set_mode((800,600))


class Settings:
    def __init__(self):
        self.no_of_life=3
        self.num_of_Enemy=100
        self.score_value=0
        self.game_starting=True
        self.game_over=False
        self.game_restart=False


s=Settings()


#explotion sound
explotion_sound=mixer.Sound(r"C:\Users\shahi\Desktop\GAME\audio\deepscanmp3-14662.mp3")
explotion_sound2=mixer.Sound(r"C:\Users\shahi\Desktop\GAME\audio\break_robot.mp3")

#hearts
life=pygame.image.load(r"C:\Users\shahi\Desktop\GAME\images\heart.png")

#background audio
mixer.music.load(r'C:\Users\shahi\Desktop\GAME\audio\spaceship-cruising-ufo-7176.mp3')
mixer.music.play(-1)

#bullet sound
bullet_sound=mixer.Sound(r'C:\Users\shahi\Desktop\GAME\audio\laserrocket2.mp3')



def heart():
    for i in range(s.no_of_life):
        screen.blit(life,(650+50*i,4))



