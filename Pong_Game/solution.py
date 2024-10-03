'''
THINGS TO REMEMBER:
# STARTING POINTS (0,0) ARE ALWAYS IN THE TOP LEFT CORNER
# IF VELOCITY IS MINUS THEN EVERYTHING GOES LEFT
# FPS -> FRAMES PER SECOND
'''

import pygame

pygame.init()

# Constant environment variables
WIDTH, HEIGHT = 700, 500
FPS = 60
BALL_RADIUS = 12

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 77)
BLUE_LIGHT = (26, 26, 255)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

SCORE_FONT = pygame.font.SysFont("Playwrite Norge", 50)
WINNING_SCORE = 2

# Window setting
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")


class Paddle:
    COLOR = BLACK
    VELOCITY = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x =  x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw_paddle(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_VELOCITY = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_velocity = self.MAX_VELOCITY
        self.y_velocity = 0

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity


    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= - 1


# Everything that's going to be drawn
def draw(window, paddles, ball, left_score, right_score):

    window.fill(BLUE)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    window.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    window.blit(right_score_text, (WIDTH * (3 / 4) + right_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw_paddle(window)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(window, BLUE_LIGHT, (WIDTH // 2 - 2, i, 10, HEIGHT // 20))

        ball.draw(window)

    # Every time something is drawn it needs to update the window
    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    # COLLISION WITH THE CEILING
    if ball.y + ball.radius >= HEIGHT:  # IF WE HIT THE BOTTOM OF THE SCREEN
        ball.y_velocity *= -1
    elif ball.y - ball.radius <= 0:  # IF WE HIT THE TOP OF THE SCREEN
        ball.y_velocity *= -1

    # COLLISION WITH THE LEFT PADDLE
    if ball.x_velocity < 0:  # IF THE BALL GOES TO THE LEFT SIDE
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_velocity *= -1  # MAKE IT MOVE TO THE RIGHT SIDE

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VELOCITY
                y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = -1 * y_velocity

    else:
        # COLLISION WITH THE RIGHTPADDLE
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velocity *= -1  # MAKE IT MOVE TO THE LEFT SIDE

                middle_y = right_paddle.y + right_paddle.height // 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VELOCITY
                y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = - 1 * y_velocity


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VELOCITY >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VELOCITY + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VELOCITY >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VELOCITY + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():

    run = True
    # Making sure it's going to run at the same speed on every pc -> FRAMES PER SEC
    clock = pygame.time.Clock()

    # Creating paddles
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    # Refreshing factor
    while run:

        clock.tick(FPS)
        draw(WINDOW, [left_paddle, right_paddle], ball, left_score, right_score)

        # Handling all the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # HANDLING THE SCORE
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        WON = False

        if left_score >= WINNING_SCORE:
            WON = True
            win_text = "LEFT PLAYER WON!"
        elif right_score >= WINNING_SCORE:
            WON = True
            win_text = "RIGHT PLAYER WON!"
        if WON:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WINDOW.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0


    pygame.quit()

if __name__ == '__main__':
    main()
