# File created by: Ryan McDonald
# Repush
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
import os
import random

vec = pg.math.Vector2

# player class
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((50,50))
        # makes the screen black 
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        # set the position of the player sprite
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # set the position of the player sprite as a 2D vector
        self.pos = vec(WIDTH/2, HEIGHT/2)
        # set the velocity of the player sprite as a 2D vector
        self.vel = vec(0,0)
        # set the acceleration of the player sprite as a 2D vector
        self.acc = vec(0,0)
        # set the coefficient of friction for the player

        self.cofric = 0.1
        self.canjump = False
        # players max health
        self.health = PLAYER_MAX_HEALTH
        self.invincible = False
        self.invincible_time = 0
    def input(self):
        # Get the state of all keyboard keys
        keystate = pg.key.get_pressed()
        # If the "a" key is pressed, set the player's x acceleration to the left
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        
    def jump(self):
        # Move the player rect to the right and check for collisions with platforms
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        # Move the player rect back to its original position
        self.rect.x -= 1
        # If the player collides with a platform, make them jump by setting their vertical velocity to a negative value
        if hits:
            self.vel.y = -PLAYER_JUMP
 
    def inbounds(self):
        # 
        if self.rect.x > WIDTH - 50:
            # 
            self.pos.x = WIDTH - 25
            # 
            self.vel.x = 0
            # 
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")
    def mob_collide(self):
        # 
        hits = pg.sprite.spritecollide(self, self.game.enemies, True)
        # 
        if hits:
            # if the player is not invincible, then they will lose 10 health everytime they collide with mob
            if not self.invincible:
                # 
                print("you have been attacked!...")
                # 
                self.game.player.health -= 10
                if self.game.player.health < 0:
                    self.game.player.health = 0


    def update(self):
        # set acceleration due to gravity
        self.acc = vec(0, PLAYER_GRAV)
        # check for collision with mobs
        self.mob_collide()
        # set friction in the x direction
        self.acc.x = self.vel.x * PLAYER_FRICTION
        # handle user input
        self.input()
        # update the velocity
        self.vel += self.acc
        # update the position using kinematic equations
        self.pos += self.vel + 0.5 * self.acc
        # update the rectangle position
        self.rect.midbottom = self.pos
        if self.invincible_time > 0:
            self.invincible_time -= 1
            if self.invincible_time == 0:
                self.invincible = False
                self.image.fill(BLACK)
                PLAYER_ACC = 2


class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.pos = vec(self.rect.center)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

# create a new platform class...


class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant

class MovingPlatform(Platform):
    # adds parameters to fit inside the plat_list
    def __init__(self, x, y, width, height, color, variant, move_speed):
        super().__init__(x, y, width, height, color, variant)
        self.move_speed = move_speed

    def update(self):
        # bounces off top and bottom of screen
        self.rect.y += self.move_speed
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.move_speed = -self.move_speed