# File created by: Ryan McDonald
    # Credit
        # Nolan Agah
        # Krisjan Harnish
# Repush
# import libraries
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from os import path
import sys
from time import sleep

# set up assets folders
game_folder = os.path.dirname(__file__)
# The purpose of the function is to render text onto a Pygame screen using the specified font size, position, and color.
def draw_text(screen, text, size, x, y, color):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        # self.load_data()
        self.score = 0
        # reate an empty sprite group for all game sprites
        self.all_sprites = pg.sprite.Group()
        # create an empty sprite group for platforms
        self.platforms = pg.sprite.Group()
        # create an empty sprite group for platforms
        self.enemies = pg.sprite.Group()
        # # create an empty sprite group for enemies
        self.player = Player(self)
        
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)

    # add the player sprite to the all_sprites group
        self.all_sprites.add(self.player)
        # iterate over a list of platform definitions
        for plat in PLATFORM_LIST:
            if len(plat) == 6:
                # create a new platform object
                p = Platform(*plat)
            # add the moving platform
            elif len(plat) == 7:
                p = MovingPlatform(*plat)
            # add the platform sprite to the all_sprites group
            self.all_sprites.add(p)
            # add the platform sprite to the platforms group
            self.platforms.add(p)
        # add all mobs
        for i in range(0,10):
             # create a new Mob object
            m = Mob(20,20,(0,255,0))
            # add the mob sprite to the all_sprites group
            self.all_sprites.add(m)
            # add the mob sprite to the enemies group
            self.enemies.add(m)
        # start the game loop
        self.run()
    def run(self):
        # set playing to True to start the game loop
        self.playing = True
        while self.playing:
            # limit the frame rate to the specified FPS
            self.clock.tick(FPS)
            # handle events such as key presses and window close events
            self.events()
            # update the game state
            self.update()
            # draw the game on the screen
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    # draws health bar
    def draw_health(self):
        # draws the health bar as a percentage of players health--see sources
        health_percentage = self.player.health / PLAYER_MAX_HEALTH
        health_width = int(health_percentage * 200)
        health_bar = pg.Rect(20, 20, health_width, 20)
        pg.draw.rect(self.screen, GREEN, health_bar)
        pg.draw.rect(self.screen, WHITE, (20, 20, 200, 20), 2)
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
        # if players health hits zero
        if self.player.health <= 0:
            # render "Game Over" text aon the screen
            draw_text(self.screen, "You Lose ", 50, WIDTH / 2, HEIGHT / 2, RED)
            pg.display.flip()
            # pause the game for 2 seconds
            sleep(2)
            # c the window
            pg.quit()
            sys.exit()
    
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # draw the 
        self.draw_text(f"Score: {self.score}", 22, WHITE, WIDTH // 2, 10)
        self.draw_health()
        pg.display.flip()
    
    # sets up draw text method
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    

# instantiate the game class
g = Game()

# start game loop
while g.running:
    g.new()

pg.quit()