import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1100, 600
ENEMY_SIZE = 40
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
ENEMY_COLOR = (0, 0, 0)
PLAYER_SIZE = 40
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
jump_strength = -12
MOVE_SPEED = 4.5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
lives = 3
coins = 0

one_player_done = False
player_gone = False
player2_gone = False

# Players
player_x, player_y = 50, 360
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
player = player_rect_img.get_rect(topleft=(player_x, player_y))
jumps_remaining = 3

player2_x, player2_y = 50, 360
player2_velocity = 0
player2_on_ground = False
player2_img = pygame.image.load("image.jpg").convert()
player2_rect_img = pygame.transform.scale(player2_img, (PLAYER_SIZE, PLAYER_SIZE))
player2 = player2_rect_img.get_rect(topleft=(player2_x, player2_y))
jumps2_remaining = 3

# Wall
wall = pygame.Rect(900, 70, 20, 330)

# Grounds
ground = pygame.Rect(0, 400, 920, 20)
ground_2 = pygame.Rect(0, 550, WIDTH, 20)

# Enemies
enemy = pygame.Rect(600, 360, ENEMY_SIZE, ENEMY_SIZE)
enemy_2 = pygame.Rect(400, 360, ENEMY_SIZE, ENEMY_SIZE)
enemy_3 = pygame.Rect(200, 360, ENEMY_SIZE, ENEMY_SIZE)
enemy_speed, enemy_2_speed, enemy_3_speed = 10, 7, 8
enemy_direction, enemy_2_direction, enemy_3_direction = 1, 1, 1

# Goal placed where spikes were
goal = pygame.Rect(500, 440, 70, 110)

# Coins
coin_size = 40
coin_img = pygame.image.load("coin.jpg").convert()
coin_1 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_1 = coin_1.get_rect(topleft=(600, 300))
coin_2 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_2 = coin_2.get_rect(topleft=(300, 50))
coin_3 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_3 = coin_3.get_rect(topleft=(950, 150))

# Clock
clock = pygame.time.Clock()

running = True
while running:
    font = pygame.font.Font(None, 60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += MOVE_SPEED
    if keys[pygame.K_a]:
        player2.x -= MOVE_SPEED
    if keys[pygame.K_d]:
        player2.x += MOVE_SPEED
    if keys[pygame.K_ESCAPE]:
        running = False

    if not player_on_ground:
        player_velocity += GRAVITY
    player.y += player_velocity

    if not player2_on_ground:
        player2_velocity += GRAVITY
    player2.y += player2_velocity

    if keys[pygame.K_UP] and player_on_ground and jumps_remaining == 3:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1
    if keys[pygame.K_SPACE] and not player_on_ground and jumps_remaining == 2:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1
    if keys[pygame.K_f] and not player_on_ground and jumps_remaining == 1:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1

    if keys[pygame.K_w] and player2_on_ground and jumps2_remaining == 3:
        player2_velocity = jump_strength
        player2_on_ground = False
        jumps2_remaining -= 1
    if keys[pygame.K_e] and not player2_on_ground and jumps2_remaining == 2:
        player2_velocity = jump_strength
        player2_on_ground = False
        jumps2_remaining -= 1
    if keys[pygame.K_q] and not player2_on_ground and jumps2_remaining == 1:
        player2_velocity = jump_strength
        player2_on_ground = False
        jumps2_remaining -= 1

    # Ground collisions
    for g in [ground, ground_2]:
        if player.colliderect(g):
            player.y = g.y - PLAYER_SIZE
            player_on_ground = True
            player_velocity = 0
            jumps_remaining = 3
        if player2.colliderect(g):
            player2.y = g.y - PLAYER_SIZE
            player2_on_ground = True
            player2_velocity = 0
            jumps2_remaining = 3

    # Coins
    for c in [coin_rect_1, coin_rect_2, coin_rect_3]:
        if player.colliderect(c) or player2.colliderect(c):
            coins += 1
            c.x = 2000

    # Goal
    if coins == 3:
        GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if player.colliderect(goal) and not player_gone:
            if one_player_done:
                import win
            else:
                one_player_done = True
                player_gone = True
                player.x = -1000  # move offscreen
                player.y = -1000

        if player2.colliderect(goal) and not player2_gone:
            if one_player_done:
                import win
            else:
                one_player_done = True
                player2_gone = True
                player2.x = -1000  # move offscreen
                player2.y = -1000

    # Enemies
    for e in [enemy, enemy_2, enemy_3]:
        if player.colliderect(e):
            lives -= 1
            player.x, player.y = 100, 360
        if player2.colliderect(e):
            lives -= 1
            player2.x, player2.y = 100, 360

    # Wall collision
    for p in [player, player2]:
        if p.colliderect(wall):
            if p.x < wall.x:
                p.x = wall.x - PLAYER_SIZE
            else:
                p.x = wall.x + wall.width

    # Enemy movement
    enemy.y += enemy_speed * enemy_direction
    if enemy.y <= 0 or enemy.y >= HEIGHT - 230:
        enemy_direction *= -1
    enemy_2.y += enemy_2_speed * enemy_2_direction
    if enemy_2.y <= 0 or enemy_2.y >= HEIGHT - 230:
        enemy_2_direction *= -1
    enemy_3.y += enemy_3_speed * enemy_3_direction
    if enemy_3.y <= 0 or enemy_3.y >= HEIGHT - 230:
        enemy_3_direction *= -1

    # Rendering
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, GROUND_COLOR, ground)
    pygame.draw.rect(screen, GROUND_COLOR, ground_2)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_2)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_3)
    pygame.draw.rect(screen, GOAL_COLOR, goal)
    pygame.draw.rect(screen, (0, 0, 0), wall)
    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)
    screen.blit(player_rect_img, player)
    screen.blit(player2_rect_img, player2)
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(lives_text, (200, 10))
    screen.blit(coins_text, (400, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
