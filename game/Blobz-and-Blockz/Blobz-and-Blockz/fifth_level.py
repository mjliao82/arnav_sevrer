import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1100, 600
PLAYER_SIZE = 40
ENEMY_SIZE = 40
ENEMY_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
JUMPPAD_COLOR = (255, 217, 3)
SPIKE_COLOR = (0, 0, 0)
PLATFORM_COLOR = (0, 0, 255)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
JUMP_STRENGTH = -12
MOVE_SPEED = 4.5
EXTRA_JUMP = -18


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

player_x = 200
player_y = 100
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
player = player_rect.get_rect(topleft=(player_x, player_y))
jumps_remaining = 3  # Number of jumps the player can perform

# Create the ground
ground_x = 0
ground_y = 400
ground_height = 20
ground = pygame.Rect(ground_x, ground_y, WIDTH - 100, ground_height)

# Create the wall
wall_x = 150
wall_y = -600
wall_width = 20
wall_height = HEIGHT + 400
wall = pygame.Rect(wall_x, wall_y, wall_width, wall_height)

# Create a platform
platform_1_y = 300
platform_1_x = 100
platform_1_width = 200
platform_1_height = 20
platform_1 = pygame.Rect(platform_1_x, platform_1_y, platform_1_width, platform_1_height)

platform_2_y = 200
platform_2_x = 800
platform_2_width = 200
platform_2_height = 20
platform_2 = pygame.Rect(platform_2_x, platform_2_y, platform_2_width, platform_2_height)

# Create a goal
goal_x = 40
goal_y = 50
goal_width = 70
goal_height = 100
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

#Create a jump pad
jumppad_x = 440
jumppad_y = 380
jumppad_width = 150
jumppad_height = 20
jumppad = pygame.Rect(jumppad_x, jumppad_y, jumppad_width, jumppad_height)

#Create an enemy
enemy_x = 600
enemy_y = 160
enemy_speed = 8
enemy_direction = 1
enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)

enemy_2_x = 400
enemy_2_y = 260
enemy_2_speed = 6
enemy_2_direction = 1
enemy_2 = pygame.Rect(enemy_2_x, enemy_2_y, ENEMY_SIZE, ENEMY_SIZE)

# Create coins
coin_size = 40
coin_img = pygame.image.load("coin.jpg").convert()
coin_1 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_1 = coin_1.get_rect(topleft=(850, 50))
coin_2 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_2 = coin_2.get_rect(topleft=(300, 260))
coin_3 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_3 = coin_3.get_rect(topleft=(500, 150))

# Clock for controlling frame rate
clock = pygame.time.Clock()
push = 5
lives = 3
coins = 0

# Game loop
running = True
while running:
    font = pygame.font.Font(None, 60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if event.type == pygame.MOUSEBUTTONUP:
            #pos = pygame.mouse.get_pos()
            #print(pos)

    # Handle player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += MOVE_SPEED
    if keys[pygame.K_ESCAPE]:
        running = False

    # Apply gravity
    if not player_on_ground:
        player_velocity += GRAVITY

    # Update player's vertical position
    player.y += player_velocity

    # Check for collisions with the ground
    if player.colliderect(ground):
        player.y = ground.y - PLAYER_SIZE
        player_on_ground = True
        player_velocity = 0
        jumps_remaining = 3

    # Check for collisions with coins
    if player.colliderect(coin_rect_1):
        coins += 1
        coin_rect_1.x = 2000
    if player.colliderect(coin_rect_2):
        coins += 1
        coin_rect_2.x = 2000
    if player.colliderect(coin_rect_3):
        coins += 1
        coin_rect_3.x = 2000

    if coins == 3:
        GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if player.colliderect(goal):
            import next_3

    # if player.colliderect(jumppad):
    #     player_velocity = EXTRA_JUMP
    #     player_on_ground = False

    if player.colliderect(enemy) or player.colliderect(enemy_2):
        lives -= 1
        player_x = 150
        player_y = 370
        player = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        if lives == 0:
            import end

    if player.x < 1:
        player.x += push

    elif player.x > 1059:
        player.x -= push

    if player.colliderect(wall):
        if player.x < wall.x:
            player.x = wall.x - PLAYER_SIZE
        else:
            player.x = wall.x + wall.width


    # Check for first jump (Up arrow)
    if keys[pygame.K_UP] and player_on_ground and jumps_remaining == 3:
        player_velocity = JUMP_STRENGTH
        player_on_ground = False
        jumps_remaining -= 1

    # Check for second jump (Spacebar)
    if keys[pygame.K_SPACE] and not player_on_ground and jumps_remaining == 2:
        player_velocity = JUMP_STRENGTH
        player_on_ground = False
        jumps_remaining -= 1

    # Check for third jump (F key)
    if keys[pygame.K_f] and not player_on_ground and jumps_remaining == 1:
        player_velocity = JUMP_STRENGTH
        player_on_ground = False
        jumps_remaining -= 1

    enemy.x += enemy_speed * enemy_direction
    if enemy.x <= 200 or enemy.x >= WIDTH:
        enemy_direction *= -1

    enemy_2.x += enemy_2_speed * enemy_2_direction
    if enemy_2.x <= 200 or enemy_2.x >= WIDTH:
        enemy_2_direction *= -1

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the ground
    pygame.draw.rect(screen, GROUND_COLOR, ground)

    #Display coins
    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)

    pygame.draw.polygon(screen, (0, 0, 0), [(1050, 530), (1020, 500), (1080, 500)])
    pygame.draw.rect(screen, (0, 0, 0), (1040, 400, 20, 100))

    # Draw the goal
    pygame.draw.rect(screen, GOAL_COLOR, goal)

    # Draw the player
    screen.blit(player_rect, player)

    # Draw the enemies
    pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_2)

    #Draw the jump pad
    pygame.draw.rect(screen, JUMPPAD_COLOR, jumppad)


    pygame.draw.rect(screen, (0, 0, 0), wall)

    #Display Lives
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (200, 10))

    #Display Coin_score
    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(coins_text, (910, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
