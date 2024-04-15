import pygame
from pygame import *


img_back = "back.png"

class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player1(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x > 5:
            self.rect.x -= self.speed


class Player2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 399:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

clock = pygame.time.Clock()
back = (200, 255, 255)

speed_x = 3
speed_y = 3

ball = GameSprite("a.png", 100, 100, 50, 50, 2)
player1 = Player2('rocket.png', 200 ,200, 100, 100, 2)



game = True
finish = False
while game:
    if finish != True:
        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player1.update_r()
        player1.reset()
        ball.reset()

        if ball.rect.y < win_height-50 or ball.rect.y < 0:
                speed_y *= -1

    time.delay(50)
    display.update()

    
    
    