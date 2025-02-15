import pygame
import random

# Initialize Pygame
pygame.init()

# Game Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game Variables
clock = pygame.time.Clock()
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
obstacle_size = 50
obstacle_pos = [random.randint(0, WIDTH - obstacle_size), 0]
obstacle_list = [obstacle_pos]
SPEED = 10

# Fonts
font = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 12
    else:
        SPEED = 15
    return SPEED

def drop_obstacles(obstacle_list):
    delay = random.random()
    if len(obstacle_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - obstacle_size)
        y_pos = 0
        obstacle_list.append([x_pos, y_pos])

def draw_obstacles(obstacle_list):
    for obstacle_pos in obstacle_list:
        pygame.draw.rect(screen, BLACK, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

def update_obstacle_positions(obstacle_list, score):
    for idx, obstacle_pos in enumerate(obstacle_list):
        if obstacle_pos[1] >= 0 and obstacle_pos[1] < HEIGHT:
            obstacle_pos[1] += SPEED
        else:
            obstacle_list.pop(idx)
            score += 1
    return score

def collision_check(obstacle_list, player_pos):
    for obstacle_pos in obstacle_list:
        if detect_collision(obstacle_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, obstacle_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    o_x = obstacle_pos[0]
    o_y = obstacle_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False

game_over = False
score = 0

# Game Loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_size
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_size

    screen.fill(WHITE)

    drop_obstacles(obstacle_list)
    score = update_obstacle_positions(obstacle_list, score)
    SPEED = set_level(score, SPEED)

    text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(text, (10, 10))

    if collision_check(obstacle_list, player_pos):
        game_over = True
        break

    draw_obstacles(obstacle_list)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()

pygame.quit()
