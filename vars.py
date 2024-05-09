import random

num_0_to_1 = random.randint(0, 1)

# ------------------------------------------------------------ SCREEN ------------------------------------------------------------- #

WIDTH=800
HEIGHT=600
EASY_MODE_INTELIGENCE = 10
MEDIUM_MODE_INTELIGENCE = 30
HARD_MODE_INTELIGENCE = 50

# ------------------------------------------------------------ PADDLE ------------------------------------------------------------- #

PLAYER_1 = "player 1"
PLAYER_2 = "player 2"
COMPUTER = "computer"

PLAYER_1_STARTING_POSITION = [(-360,40), (-360,20), (-360,0), (-360,-20), (-360,-40)]
PLAYER_2_STARTING_POSITION = [(360,40), (360,20), (360,0), (360,-20), (360,-40)]
BALL_STARTING_POSITION = (0, -150)
PLAYER_SPEED = 40
COMPUTER_SPEED = 40
PADDLE_WIDTH = 1.2
PADDLE_HEIGHT = 1.2

# ------------------------------------------------------------ ANGLES ------------------------------------------------------------- #

NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
NORTH_EAST = 45
NORTH_WEST = 90 + 45
SOUTH_WEST = 180 + 45
SOUTH_EAST = 270 + 45
N = "N"
S = "S"
W = "W"
E = "E"
NE = "NE"
NW = "NW"
SW = "SW"
SE = "SE"

# ------------------------------------------------------------ BALL ------------------------------------------------------------- #


initial_ball_travel = [NW, NE]
initial_paddle_travel = [N, S]
angle_start = [NORTH_WEST, NORTH_EAST]
direction = [NORTH, SOUTH]
INITIAL_BALL_TRAVEL = initial_ball_travel[num_0_to_1]
INITIAL_PADDLE_TRAVEL = initial_paddle_travel[num_0_to_1]
DIRECTION = direction[num_0_to_1]
BALL_STARTING_ANGLE = angle_start[num_0_to_1]
MEDIUM_BALL_SPEED = 20
FAST_BALL_SPEED = 30
BALL_WIDTH = 0.5
BALL_HEIGHT = 0.5

# ------------------------------------------------------------ TEXTBOARD ------------------------------------------------------------- #

PLAYER_SCORE_POSITION = (-80, 230)
COMPUTER_SCORE_POSITION = (80, 230)
SCORE_FONT = ("Arial", 24, "normal")
TEXT_FONT = ("Arial", 18, "bold")
FIRST_TO_X = ("Arial", 14, "normal")
MAX_SCORE = 3