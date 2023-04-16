# File created by: Ryan McDonald
# Repush
WIDTH = 1300
HEIGHT = 900
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
PINK = (255,0,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (500, 350, 100, 20, (200,200,200), "normal"),
                 (0, 130, 1200, 20, (200,200,200), "normal"),
                 (30, 200, 1250, 20, (200,200,200), "normal"),
                 (800, 600, 25, 20, (255,50,255), "normal"),
                 (100, 700, 25, 20, (255,50,255), "normal"),
                 (200, 350, 100, 5, (255,50,255), "normal")]

# x, y, width, height, color, variant):