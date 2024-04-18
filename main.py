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
fake = True
run = True
clock = time.Clock()
FPS = 60
finish = False
win1 = 0
win2 = 0
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed_x,player_speed_y,player_weight,player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_weight, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.weight = player_weight
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed_y
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed_y        
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        global win1
        global win2
        if self.rect.y == 420:
            self.speed_y *= -1
        if self.rect.y == 0:
            self.speed_y *= -1
        if sprite.collide_rect(player1, ball):
            self.speed_x *= -1
        if sprite.collide_rect(player2, ball):
            self.speed_x *= -1
        if self.rect.x <= 0:
            win1 = win1 + 1
        if self.rect.x >= 500:
            win2 = win2 + 1       
player1 = Player1('player2.jpg',70,250,0,5,20,150)
player2 = Player2('player2.jpg',420,250,0,5,20,150)
ball = Ball('Ball.jpg',250,350,2,2,70,70)
while run:
    if fake == True:
        window.blit(background,(0,0))
        text_loby = font2.render('НАЧАТЬ ИГРУ', 1, (0,255,0))
        window.blit(text_loby,(100,200))
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_b:
                    fake = False
                    finish = True
    for e in event.get():
            if e.type == QUIT:
                run= False
    if finish != False:
        window.blit(background,(0,0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()   
        if win1 == 1:
            text_super_win = font2.render('ПОБЕДА 1!', 1, (0,255,0))
            finish = False
            window.blit(text_super_win,(100,200))
        if win2 == 1:
            text_super_win = font2.render('ПОБЕДА 2!', 1, (0,255,0))
            finish = False
            window.blit(text_super_win,(100,200))
    clock.tick(FPS)
    display.update()
