import pygame
from ball import Circle

size = WIDTH, HEIGHT = 900, 600

WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Ping-Pong")

BLOCK_WIDTH = 30
BLOCK_HEIGHT = 100

BLACK = (0, 0, 0)

GREEN = (0, 255, 0)

WHITE = (255, 255, 255)

BLOCK_SPEED = 10

FPS = 60

bounds = WIN.get_rect()


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


def ball_movement(bounds, ball):
    ball.x += ball.vel_x
    ball.y += ball.vel_y

    if ball.x - ball.radius < bounds.left or ball.x + ball.radius > bounds.right:
        ball.vel_x *= -1
    if ball.y - ball.radius < bounds.top or ball.y + ball.radius > bounds.bottom:
        ball.vel_y *= -1


def draw_window(block1, block2, ball):
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, GREEN, block1)
    pygame.draw.rect(WIN, GREEN, block2)

    pygame.draw.circle(WIN, WHITE, (ball.x, ball.y), ball.radius)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    block1 = pygame.Rect(20, HEIGHT//2 - BLOCK_HEIGHT//2, BLOCK_WIDTH, BLOCK_HEIGHT)
    block2 = pygame.Rect(WIDTH-20-BLOCK_WIDTH, HEIGHT//2 - BLOCK_HEIGHT//2, BLOCK_WIDTH, BLOCK_HEIGHT)

    ball = Circle(450, 300, 10)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        left_block_movement(keys_pressed, block1)
        right_block_movement(keys_pressed, block2)

        ball_movement(bounds, ball)

        draw_window(block1, block2, ball)

    pygame.quit()


if __name__ == "__main__":
    main()