import pygame

import config

pygame.init()

win = pygame.display.set_mode((750, 500))

loseSpr = pygame.image.load("sprites/final_screen/lose.png")
restartBtn = [pygame.image.load("sprites/button/restart/restart0.png"), pygame.image.load("sprites/button/restart/restart1.png")]
menuBtn = [pygame.image.load("sprites/button/button_of_back/button_back_of_menu.png"), pygame.image.load("sprites/button/button_of_back/button_back_of_menu1.png")]

fon = pygame.image.load("sprites/logo/fons/fon_progect.png")

def static():
    win.blit(fon, (0, 0))
    win.blit(loseSpr, (50, 10))

def restart(pos, press):
    x = 288
    y = 200
    if(pos[0] > x and pos[0] < x + 168 and pos[1] > y and pos[1] < y + 56):
        win.blit(restartBtn[1], (x, y))
        if(press == True):
            config.config["scene"] = "play"
    else:
        win.blit(restartBtn[0], (x, y))

def menu(pos, press):
    x = 308
    y = 300
    if(pos[0] > x and pos[0] < x + 130 and pos[1] > y and pos[1] < y + 60):
        win.blit(menuBtn[1], (x, y))
        if(press == True):
            config.config["scene"] = "menu"
    else:
        win.blit(menuBtn[0], (x, y))