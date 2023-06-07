import pygame

import config
import menu
import play
import git
import wingame
import losegame

pygame.init()
win = pygame.display.set_mode((750, 500))
pygame.display.set_icon(pygame.image.load("sprites/logo/icon_of_game.png"))

pygame.display.set_caption("MineSweeper")

clock = pygame.time.Clock()
FPS = 30

while(config.config["global_run"] == True): #цикл игры
    clock.tick(FPS)
    press = False
    scene = config.config["scene"] #определение сцены
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.config["global_run"] = False
        if event.type == pygame.MOUSEBUTTONUP:
            press = True

    win.fill((230,230,230))
    pos = pygame.mouse.get_pos()#la voiture noire

    if(scene == "menu"): #отображение экрана в зависимости от сцены
        menu.static()
        menu.playBtn(pos, press)
        menu.githubBtn(pos, press)
    if(scene == "play"):
        play.startGame()
    if(scene == "git"):
        git.githubbtn(pos, press)
    if(scene == "win"):
        wingame.static()
        wingame.restart(pos, press)
        wingame.menu(pos, press)
    if(scene == "lose"):
        losegame.static()
        losegame.restart(pos, press)
        losegame.menu(pos, press)

    pygame.display.update() #обновление экрана