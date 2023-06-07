import pygame

import config

pygame.init()
win = pygame.display.set_mode((750, 500))

#спрайты
play = [pygame.image.load("sprites/button/play/play0.png"), pygame.image.load("sprites/button/play/play1.png")]
logo1 = pygame.image.load("sprites/logo/MineSweeper.png")
buttonOfGit = [pygame.image.load("sprites/button/button_of_git/button_of_git.png"), pygame.image.load("sprites/button/button_of_git/button_take2.png")]
fon = pygame.image.load("sprites/logo/fons/fon_progect.png")

text = pygame.font.SysFont("Impact", 20)

def static(): #статические эллементы
    win.blit(fon, (0, 0))
    win.blit(logo1, (50, 60))
    win.blit(text.render(config.config["version"], 1, (107, 50, 0), (255,255,255)), (710, 470))

def playBtn(pos, press): #кнопка игры
    x = 288
    y = 200
    if(pos[0] > x and pos[0] < x + 168 and pos[1] > y and pos[1] < y + 56):
        win.blit(play[1], (x, y))
        if(press == True):
            config.config["scene"] = "play" #меняет сцену
    else:
        win.blit(play[0], (x, y))

def githubBtn(pos, press):
    x = 288
    y = 270
    if(pos[0] > x and pos[0] < x + 168 and pos[1] > y and pos[1] < y + 56):
        win.blit(buttonOfGit[1], (x, y))
        if(press == True):
            config.config["scene"] = "git"
    else:
        win.blit(buttonOfGit[0], (x, y))
