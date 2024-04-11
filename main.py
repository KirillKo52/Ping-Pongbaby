from pygame import *
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
font.init()
font1 = font.SysFont('Arial', 36)
lost = 0
win = 0
HP = 3
font2 = font.SysFont('Arial', 50)
window = display.set_mode((500,500))
display.set_caption('Maze')
background = transform.scale(image.load("images.jpeg"),(500,500))
'''mixer.init()
mixer.music.load('game.ogg')
mixer.music.play()'''
run = True
clock = time.Clock()
FPS = 60
finish = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speedx,player_speedy,player_weight,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_weight, player_height))
        self.speed.x = player_speedx
        self.speed.y = player_speedy
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
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed        
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y = 450:
            self.speedy * -1
        if self.rect.y = 50:
            self.speedy * -1
        if self.rect.x = 70:
            self.speedx * -1
        if self.rect.x = 420:
            self.speedx * -1
player1 = Player1('player2.jpg',70,250,5,20,150)
player2 = Player2('player2.jpg',420,250,5,20,150)
ball = Ball('Ball.jpg',250,350,1,70,70)
while run:
    for e in event.get():
        if e.type == QUIT:
            run= False
    if run != False:
        window.blit(background,(0,0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
    clock.tick(FPS)
    display.update()
