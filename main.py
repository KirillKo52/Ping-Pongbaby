from pygame import *
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
font.init()
font1 = font.SysFont('Arial', 36)
lost = 0
win = 0
HP = 3
font2 = font.SysFont('Arial', 100)
window = display.set_mode((700,700))
display.set_caption('Maze')
background = transform.scale(image.load("ZadniyFon.jpg"),(700,500))
mixer.init()
mixer.music.load('game.ogg')
mixer.music.play()
run = True
clock = time.Clock()
FPS = 60
finish = True
fake = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_weight,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_weight, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.weight = player_weight
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 615:
            self.rect.x += self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < 615:
            self.rect.x += self.speed        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,620)
            lost = lost + 1
        self.speed = randint(1,2)