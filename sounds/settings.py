# File created by: Ryan McDonald
# Repush
# how wide
WIDTH = 1300
# height of screen
HEIGHT = 900
# for fast player goes
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
# how high player jumps
PLAYER_JUMP = 20
# how fast player can fall
PLAYER_GRAV = 0.8
# for fast mob goes
MOB_ACC = 2
# mob friction
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
PINK = (255,0,50)
# color 
GREEN = (0, 128, 0)
# frames per second
FPS = 60
RUNNING = True
# your score
SCORE = 0
PAUSED = False
# player health
PLAYER_MAX_HEALTH = 100

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"), 
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (500, 350, 100, 20, (200,200,200), "normal"), 
                 (500, 130, 600, 20, (200,200,200), "normal"),
                 (30, 200, 700, 20, (200,200,200), "normal"),
                 (800, 600, 25, 20, (255,50,255), "normal"),
                 (100, 700, 25, 20, (255,50,255), "normal"),
                 (200, 350, 100, 5, (255,50,255), "normal")]

# x, y, width, height, color, variant):