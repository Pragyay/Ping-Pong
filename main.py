import pygame
pygame.init()

size = WIDTH, HEIGHT = 1080, 600

WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Ping-Pong")

POINTS_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

BLOCK_WIDTH = 30
BLOCK_HEIGHT = 100

BLACK = (0, 0, 0)

GREEN = (0, 255, 0)

WHITE = (255, 255, 255)

BLOCK_SPEED = 20

FPS = 60

LEFT_POINT = pygame.USEREVENT + 1
RIGHT_POINT = pygame.USEREVENT + 2

ball_image = pygame.image.load('ball.png')
ball_image = pygame.transform.scale(ball_image, (20, 20))


def left_block_movement(keys_pressed, block1):
    if keys_pressed[pygame.K_w] and block1.y > 10:
        block1.y -= BLOCK_SPEED
    if keys_pressed[pygame.K_s] and block1.y + BLOCK_HEIGHT + 10 < HEIGHT:
        block1.y += BLOCK_SPEED


def right_block_movement(keys_pressed, block2):
    if keys_pressed[pygame.K_UP] and block2.y > 10:
        block2.y -= BLOCK_SPEED
    if keys_pressed[pygame.K_DOWN] and block2.y + BLOCK_HEIGHT + 10 < HEIGHT:
        block2.y += BLOCK_SPEED


# def ball_movement(ball, ball_vel_x, ball_vel_y, bounds):
#     ball.x += ball_vel_x
#     ball.y += ball_vel_y
#
#     if ball.x < bounds.left or ball.x > bounds.right:
#         ball_vel_x *= -1
#     if ball.y < bounds.top or ball.y > bounds.bottom:
#         ball_vel_y *= -1

# def collision(block1, block2, ball):
#     if ball.collideRect(block1):
#         ball_vel_x *= 1
#     if ball.collideRect(block2):
#         ball_vel_x *= 1

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_window(block1, block2, ball, left_points, right_points):
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, GREEN, block1)
    pygame.draw.rect(WIN, GREEN, block2)

    WIN.blit(ball_image, (ball.x, ball.y))

    l_points = POINTS_FONT.render("Points: " + str(left_points), 1, WHITE)
    r_points = POINTS_FONT.render("Points: " + str(right_points), 1, WHITE)

    WIN.blit(l_points, (WIDTH//2 - l_points.get_width() - 10, 20))
    WIN.blit(r_points, (WIDTH//2 + 10, 20))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    block1 = pygame.Rect(20, HEIGHT//2 - BLOCK_HEIGHT//2, BLOCK_WIDTH, BLOCK_HEIGHT)
    block2 = pygame.Rect(WIDTH-20-BLOCK_WIDTH, HEIGHT//2 - BLOCK_HEIGHT//2, BLOCK_WIDTH, BLOCK_HEIGHT)

    ball = pygame.Rect(450, 300, 20, 20)

    ball_vel_x = 15
    ball_vel_y = 15

    bounds = WIN.get_rect()

    left_points = 0
    right_points = 0

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == LEFT_POINT:
                left_points += 1

            if event.type == RIGHT_POINT:
                right_points += 1

        winner_text = ""
        if left_points > 10:
            winner_text = "Left wins!"
        if right_points > 10:
            winner_text = "Right wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        left_block_movement(keys_pressed, block1)
        right_block_movement(keys_pressed, block2)

        ball.x += ball_vel_x
        ball.y += ball_vel_y
        if ball.x < bounds.left:
            pygame.event.post(pygame.event.Event(RIGHT_POINT))
            ball_vel_x *= -1
        if ball.x > bounds.right:
            pygame.event.post(pygame.event.Event(LEFT_POINT))
            ball_vel_x *= -1
        if ball.y < bounds.top or ball.y > bounds.bottom:
            ball_vel_y *= -1

        if ball.colliderect(block1):
            ball_vel_x *= -1
        if ball.colliderect(block2):
            ball_vel_x *= -1

        draw_window(block1, block2, ball, left_points, right_points)

    pygame.quit()


if __name__ == "__main__":
    main()