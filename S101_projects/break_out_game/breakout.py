"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global Variable
score = 0
score_label = GLabel('Score=>'+str(score))
live_label = GLabel('Live: '+str(NUM_LIVES))


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    # Score Label
    global score
    score_label.font = '-15'
    graphics.window.add(score_label, x=0, y=graphics.window.height-10)
    # Live Label
    live = NUM_LIVES
    live_label.font = '-15'
    graphics.window.add(live_label, x=graphics.window.width-75, y=graphics.window.height - 10)

    y_bound = graphics.window.height-graphics.p_off-graphics.paddle.height-graphics.b_r*2
    # Num of bricks be hit
    count = 0

    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        pause(FRAME_RATE)
        graphics.ball.move(vx, vy)
        # X-Direction Boundary
        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            graphics.set_vx()
        # Y-Direction Boundary
        elif graphics.ball.y <= 0:
            graphics.set_vy()
        # # While hit on paddle
        # elif graphics.paddle.x - graphics.b_r < graphics.ball.x + graphics.b_r < graphics.paddle.x \
        #         + graphics.p_width + graphics.b_r and graphics.window.height - graphics.p_off \
        #         - graphics.paddle.height <= graphics.ball.y + graphics.b_r * 2:
        #     if graphics.ball.y + graphics.b_r >= graphics.window.height - graphics.p_off \
        #            - graphics.paddle.height:
        #         if graphics.paddle.x + graphics.p_width < graphics.ball.x + graphics.b_r or graphics.ball.x \
        #                 + graphics.b_r + graphics.paddle.x:
        #             vx = -vx * 1.02
        #             vy = -vy
        #     else:
        #         vy = -vy
        # While ball out of bound
        elif graphics.ball.y > graphics.window.height:
            live -= 1
            live_label.text = 'Live: ' + str(live)
            graphics.reset_ball()

        # End game condition
        elif live == 0 or count >= graphics.n_brick:
            break
        check_collision(graphics)
        # else:
        #     # Get ball collision at four corners
        #     obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        #     obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        #     obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.b_r*2)
        #     obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)
        #     if obj1 is not None:
        #         if obj1 is not graphics.paddle and obj1 is not score_label and obj1 is not live_label:
        #             graphics.set_vy()
        #             graphics.window.remove(obj1)
        #             count += 1
        #             score += graphics.score_add_on()
        #             score_label.text = 'Score==>'+str(score)
        #         elif obj1 is graphics.paddle:
        #             if graphics.get_vy() > 0:
        #                 graphics.set_vy()
        #     elif obj2 is not None:
        #         if obj2 is not graphics.paddle and obj2 is not score_label and obj2 is not live_label:
        #             graphics.set_vy()
        #             graphics.window.remove(obj2)
        #             count += 1
        #             score += graphics.score_add_on()
        #             score_label.text = 'Score==>' + str(score)
        #         elif obj2 is  graphics.paddle:
        #             if graphics.get_vy() > 0:
        #                 graphics.set_vy()
        #
        #     elif obj3 is not None:
        #         if obj3 is not graphics.paddle and obj3 is not score_label and obj3 is not live_label:
        #             graphics.set_vy()
        #             graphics.window.remove(obj3)
        #             count += 1
        #             score += graphics.score_add_on()
        #             score_label.text = 'Score==>' + str(score)
        #         elif obj3 is graphics.paddle:
        #             if graphics.get_vy() > 0:
        #                 graphics.set_vy()
        #     elif obj4 is not None:
        #         if obj4 is not graphics.paddle and obj4 is not score_label and obj4 is not live_label:
        #             graphics.set_vy()
        #             graphics.window.remove(obj4)
        #             count += 1
        #             score += graphics.score_add_on()
        #             score_label.text = 'Score==>' + str(score)
        #         elif obj4 is graphics.paddle:
        #             if graphics.get_vy() > 0:
        #                 graphics.set_vy()


def check_collision(graphics):
    global score
    for x in range(graphics.ball.x, graphics.ball.x+graphics.ball.width+1, graphics.ball.width):
        for y in range(graphics.ball.y, graphics.ball.y+graphics.ball.height+1, graphics.ball.height):
            obj = graphics.window.get_object_at(x, y)
            if obj is not None:
                if obj is not graphics.paddle and obj is not score_label and obj is not live_label:
                    graphics.set_vy()
                    graphics.window.remove(obj)
                    graphics.brick_num -= 1
                    score += graphics.score_add_on()
                    score_label.text = 'Score==>' + str(score)
                elif obj is graphics.paddle:
                    if graphics.get_vy() > 0:
                        graphics.set_vy()


if __name__ == '__main__':
    main()
