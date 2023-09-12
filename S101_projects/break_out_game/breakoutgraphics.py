"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.b_r = ball_radius
        self.p_off = paddle_offset
        self.p_width = paddle_width
        self.p_height = paddle_height
        self.n_brick = BRICK_ROWS * BRICK_COLS
        self.pt = 0
        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'gray'
        self.window.add(self.paddle, x=self.window.width/2 - paddle_width/2, y=self.window.height - paddle_offset)
        # Center a filled ball in the graph, ical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.ball.color = 'black'
        self.window.add(self.ball, x=self.window.width // 2 - self.ball.width//2, y=self.window.height //2 - self.ball.height//2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_out_bound = self.ball.y + BALL_RADIUS * 2 > self.window.height - PADDLE_OFFSET
        self.switch = True
        self.brick_num = brick_cols*brick_rows
        # Initialize our mouse listeners
        onmouseclicked(self.action_start)  # onmouseclicked()
        onmousemoved(self.set_position)  # onmousemoved()
        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                # Bricks Color Setting
                if j == 0 or j == 1:
                    self.brick.fill_color = 'red'
                elif j == 2 or j == 3:
                    self.brick.fill_color = 'orange'
                elif j == 4 or j == 5:
                    self.brick.fill_color = 'yellow'
                elif j == 6 or j == 7:
                    self.brick.fill_color = 'green'
                elif j == 8 or j == 9:
                    self.brick.fill_color = 'blue'

                self.window.add(self.brick, x=(brick_spacing+brick_width)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)

    def set_position(self, mouse):
        if mouse.x >= self.window.width - PADDLE_WIDTH / 2:
            self.paddle.x = self.window.width - PADDLE_WIDTH
        elif mouse.x <= 0 + PADDLE_WIDTH / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        return self.paddle.x

    def action_start(self, event):
        if self.switch:
            obj = self.window.get_object_at(event.x, event.y)
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.randint(0, 1) > 0.5:
                self.__dx = -self.__dx
            self.switch = False

    # def ball_out(self):
    #     ball_out_bound = self.ball.y + self.b_r * 2 >= self.window.height - self.p_off/2
    #     return ball_out_bound

    def reset_ball(self):
        self.window.add(self.ball, x=self.window.width // 2 - self.ball.width//2, y=self.window.height //2 - self.ball.height//2)
        self.switch = True
        self.__dx = self.__dy = 0

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self):
        self.__dx = -self.__dx

    def set_vy(self):
        self.__dy = -self.__dy

    def score_add_on(self):
        level = BRICK_HEIGHT+BRICK_SPACING
        if self.ball.y < level:
            self.pt = 10
        elif BRICK_OFFSET + level <= self.ball.y < BRICK_OFFSET + level * 2:
            self.pt = 9
        elif BRICK_OFFSET + level * 2 <= self.ball.y < BRICK_OFFSET + level * 3:
            self.pt = 8
        elif BRICK_OFFSET + level * 3 <= self.ball.y < BRICK_OFFSET + level * 4:
            self.pt = 7
        elif BRICK_OFFSET + level * 4 <= self.ball.y < BRICK_OFFSET + level * 5:
            self.pt = 6
        elif BRICK_OFFSET + level * 5 <= self.ball.y < BRICK_OFFSET + level * 6:
            self.pt = 5
        elif BRICK_OFFSET + level * 6 <= self.ball.y < BRICK_OFFSET + level * 7:
            self.pt = 4
        elif BRICK_OFFSET + level * 7 <= self.ball.y < BRICK_OFFSET + level * 8:
            self.pt = 3
        elif BRICK_OFFSET + level * 8 <= self.ball.y < BRICK_OFFSET + level * 9:
            self.pt = 2
        elif BRICK_OFFSET + level * 9 <= self.ball.y < BRICK_OFFSET + level * 10:
            self.pt = 1

        return self.pt




