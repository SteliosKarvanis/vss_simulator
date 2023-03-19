#colors
BACKGROUND_COLOR = (0, 0, 0)
ENEMY_PLAYER_COLOR = (255, 0, 0)
ALLY_PLAYER_COLOR = (0, 150, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
DARK_GRAY = (105,105,105)

#Ball
BALL_RADIUS = 15

#Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

#Field
FIELD_WIDTH = SCREEN_WIDTH
FIELD_HEIGHT = 720

#Status bar
STATUS_HEIGHT = SCREEN_HEIGHT - FIELD_HEIGHT

#Scoreboard
SCOREBOARD_HEIGHT =  round(1.5*STATUS_HEIGHT)
BOARD_IMG_RESOLUTION = (5064, 2422)
CLOCK_ORIGINAL_POS = (1870, 1230)
CLOCK_POS = (round(CLOCK_ORIGINAL_POS[0]/BOARD_IMG_RESOLUTION[1]*SCOREBOARD_HEIGHT),round(CLOCK_ORIGINAL_POS[1]/BOARD_IMG_RESOLUTION[1]*SCOREBOARD_HEIGHT))
CLOCK_FRAME_HEIGHT = round(SCOREBOARD_HEIGHT*0.29)
DIGIT_WIDTH = round(CLOCK_FRAME_HEIGHT*0.42)
CLOCK_CENTER = (CLOCK_POS[0] + 2.25*DIGIT_WIDTH, CLOCK_POS[1] + CLOCK_FRAME_HEIGHT/2)
CLOCK_DIGIT_POSITIONS = [CLOCK_POS,(CLOCK_POS[0]+DIGIT_WIDTH,CLOCK_POS[1]),(CLOCK_POS[0]+DIGIT_WIDTH*2.5,CLOCK_POS[1]),(CLOCK_POS[0]+DIGIT_WIDTH*3.5,CLOCK_POS[1])]

#Player
PLAYER_SIZE = (50, 50)
PLAYER_LINEAR_SPEED = .3
PLAYER_ANGULAR_SPEED = .3
PLAYER_SPIN_SPEED = 2
PLAYER_SPIN_COUNTDOWN = 100