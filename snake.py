#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:40:10 2020

@author: paul
"""
import pygame
#from time import sleep
from random import randint

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Snake')
clock = pygame.time.Clock()   

class snake(object):
    
    def __init__(self):
        self.size = 10
        self.y_positions = [250, 240, 230]
        self.x_positions = [250 ,250, 250]
        self.color = (255,0,0)
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    
        
    def draw(self, win):
        #drawing snake
        for i in range(len(self.y_positions)):
                pygame.draw.rect(win, self.color, (self.x_positions[i], self.y_positions[i], self.size, self.size))
    
    def move(self):
        
        #moving snake
        if self.up:
            self.y_positions.insert(0, self.y_positions[0]-10)
            self.x_positions.insert(0, self.x_positions[0])
            self.removing_last()
            
        elif self.left:
            self.x_positions.insert(0, self.x_positions[0]-10)
            self.y_positions.insert(0, self.y_positions[0])
            self.removing_last()
        
        elif self.down:
             self.y_positions.insert(0, self.y_positions[0]+10)
             self.x_positions.insert(0, self.x_positions[0])
             self.removing_last()
             
        elif self.right:
            self.x_positions.insert(0, self.x_positions[0]+10)
            self.y_positions.insert(0, self.y_positions[0])
            self.removing_last()
            
    def removing_last(self):
        self.x_positions.pop()
        self.y_positions.pop()
    #detecting collisions
    def collide_food(self):
        if self.x_positions[0] == apple.x and self.y_positions[0] == apple.y:
            self.append()
            score_board.score += 10
            apple.food_status = True
            
    def collide_border(self):
        if self.x_positions[0] < 0 or self.x_positions[0] > 500:
            return True
              
        if self.y_positions[0] < 0 or self.y_positions[0] > 500:
            return True
        
    def collide_self(self):
        for i in range(len(self.x_positions)-2):
            if self.x_positions[0] == self.x_positions[i+2] and self.y_positions[0] == self.y_positions[i+2]:
                return True
            
    #appending snake
    def append(self):
        if self.right:
            self.x_positions.append(self.x_positions[-1]-10)
            self.y_positions.append(self.y_positions[-1])
            
        if self.left:
            self.x_positions.append(self.x_positions[-1]+10)
            self.y_positions.append(self.y_positions[-1])
        
        if self.up:
            self.x_positions.append(self.x_positions[-1])
            self.y_positions.append(self.y_positions[-1]+10)
        
        if self.down:
            self.x_positions.append(self.x_positions[-1])
            self.y_positions.append(self.y_positions[-1]-10)
    
    
    
    
class food(object):
    
    def __init__(self):
        self.size = 10
        self.food_status = True
        self.color = (0,255,0)
        self.x = 250
        self.y = 100
        
    def create(self):
        self.x = randint(1,49)*10
        self.y = randint(1,49)*10
        self.food_status = False
        
    def draw(self, win):
        #appears random on screen
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))
        
    
    
class score:
    def __init__(self):
        self.score = 0
        self.myfont = pygame.font.SysFont("monospace", 25)
    
    def draw(self, win):
        label = self.myfont.render(f"{self.score}", 1, (255,255,255))
        win.blit(label, (450, 25))
    
    #shows score
    
    #gets score om snake length
    
def updateScreen():
    win.fill((0,0,0))
    anaconda.move()
    anaconda.draw(win)
    score_board.draw(win)
    apple.draw(win)
        
    pygame.display.update()
 
apple = food()
anaconda = snake()
score_board = score()
run = True
start = False
    
while run:
    
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
         
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and start == True:
        anaconda.down = False
        anaconda.up = True
        anaconda.right = False
        anaconda.left = False
        
    elif keys[pygame.K_DOWN]:
        anaconda.down = True
        anaconda.right = False
        anaconda.left = False
        anaconda.up = False
        start = True
        
    elif keys[pygame.K_RIGHT]:
        anaconda.down = False
        anaconda.right = True
        anaconda.left = False
        anaconda.up = False
        start = True
        
    elif keys[pygame.K_LEFT]:
        anaconda.down = False
        anaconda.left = True
        anaconda.right = False
        anaconda.up = False
        start = True
        
    elif keys[pygame.K_SPACE]:
        anaconda.removing_last()
    
    
    #detecting collisions
    
    anaconda.collide_food()
    
    if anaconda.collide_border():
        print('You Lost')
        print(f'your score was {score_board.score}')
        run = False
    if anaconda.collide_self():
        print('You Lost')
        print(f'your score was {score_board.score}')
        run = False
        
    #creating new food
    if apple.food_status:
        apple.create()
    
    updateScreen()

pygame.quit()