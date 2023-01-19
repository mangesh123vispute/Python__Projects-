import random                                   #for generating random number
import sys
import pygame
from pygame.locals import *

# global variables for the game

fps=32 # this is frames per second
screenwidth=200
screenheight=200
screen=pygame.display.set_mode((screenwidth,screenheight))
groundy=screenheight*0.8
game_sprites={}
game_sounds={}
player='gallery/sprites/bird.png'
background='gallery/sprites/background.png'
pipe='gallery/sprites/pipe.png'

def welcomescreen():
    '''shows welcome images on the screen '''
    playerx=int(screenwidth/5)
    playery=int(screenheight-game_sprites['player'].get_height())/2
    
    pass





# this will be the    main point from where   our game will start
if __name__ == '__main__':
    pygame.init()          #initilize all pygame modules
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption('flappy game by mangesh')
    game_sprites['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )
    game_sprites['message']= pygame.image.load('gallery/sprites/message.png').convert_alpha()
    game_sprites['base']=pygame.image.load('gallery/sprites/base.png').convert_alpha()
    game_sprites['pipe']=(
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180),
        pygame.image.load(pipe).convert_alpha()
    )
    # game sounds
    game_sounds['die']=pygame.mixer.Sound('gallery/audio/die.wav')
    game_sounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    game_sounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    game_sounds['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    game_sounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    game_sprites['background']=pygame.image.load(background).convert()
    game_sprites['player']=pygame.image.load(player).convert_alpha()






