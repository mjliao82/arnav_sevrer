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
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
PLATFORM_COLOR = (0, 0, 255)
JUMPPAD_COLOR = (255, 217, 3)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
JUMP_STRENGTH = -12
MOVE_SPEED = 4.5
EXTRA_JUMP = -18

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
lives = 3
coins = 0

# Create the player character
player_x = 350
player_y = 100
player_size = 40
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect = pygame.transform.scale(player_img, (player_size, player_size))
player = player_rect.get_rect(topleft=(player_x, player_y))

# Create the wall
wall_x = 900
wall_y = -1115
wall_width = 20
wall_height = 1500
wall = pygame.Rect(wall_x, wall_y, wall_width, wall_height)

# Create the ground
ground_x = 0
ground_y = 400
ground_height = 20
ground = pygame.Rect(ground_x, ground_y, WIDTH, ground_height)

#Create an enemy
enemy_x = 500
enemy_y = 360
enemy_speed = 10
enemy_direction = 1
enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)

# Create a platform
platform_1_y = 100
platform_1_x = 700
platform_1_width = 200
platform_1_height = 20
platform_1 = pygame.Rect(platform_1_x, platform_1_y, platform_1_width, platform_1_height)

platform_2_y = 300
platform_2_x = 000
platform_2_width = 200
platform_2_height = 20
platform_2 = pygame.Rect(platform_2_x, platform_2_y, platform_2_width, platform_2_height)

#Create a jump pad
jumppad_x = 440
jumppad_y = 380
jumppad_width = 150
jumppad_height = 20
jumppad_speed = 5
jumppad_direction = 1
jumppad = pygame.Rect(jumppad_x, jumppad_y, jumppad_width, jumppad_height)

#Create a jump pad
jumppad_2_x = 950
jumppad_2_y = 380
jumppad_2_width = 100
jumppad_2_height = 20
jumppad_2 = pygame.Rect(jumppad_2_x, jumppad_2_y, jumppad_2_width, jumppad_2_height)

# Create a goal
goal_x = 950
goal_y = 25
goal_width = 70
goal_height = 100
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

#Create coins
coin_size = 40
coin_img = pygame.image.load("coin.jpg").convert()
coin_1 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_1 = coin_1.get_rect(topleft=(600, 300))
coin_2 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_2 = coin_2.get_rect(topleft=(300, 50))
coin_3 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_3 = coin_3.get_rect(topleft=(950, 150))

# Clock for controlling frame rate
clock = pygame.time.Clock()
push = 5
small = False
double_jump = True


# Game loop
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
    if keys[pygame.K_ESCAPE]:
        running = False

    if not player_on_ground:
        player_velocity += GRAVITY
    player.y += player_velocity

    if keys[pygame.K_UP]:
        if player_on_ground or not double_jump:
            if not player_on_ground:
                double_jump = True
            player_velocity = JUMP_STRENGTH
            player_on_ground = False

    if double_jump:
        if keys[pygame.K_UP]:
            player_velocity = JUMP_STRENGTH
            player_on_ground = False
            if keys[pygame.K_SPACE]:
                player_velocity = JUMP_STRENGTH
                player_on_ground = False
                if keys[pygame.K_f]:
                    player_velocity = JUMP_STRENGTH
                    player_on_ground = False
            
            

    if player.colliderect(ground):
        player.y = ground.y - player_size
        player_on_ground = True
        player_velocity = 0

    if (player.y < platform_1_y and player.y > (platform_1_y - player_size)) and (player.x > platform_1_x and player.x < platform_1_x + platform_1_width):
        player.y = platform_1.y - player_size
        player_on_ground = True
        player_velocity = 0

    if (player.y < platform_2_y and player.y > (platform_2_y - player_size)) and (player.x > platform_2_x and player.x < platform_2_x + platform_2_width):
        player.y = platform_2.y - player_size
        player_on_ground = True
        player_velocity = 0

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
            import win

    if player.colliderect(jumppad):
        player_velocity = EXTRA_JUMP
        player_on_ground = False

    if player.colliderect(jumppad_2):
        player_velocity = EXTRA_JUMP
        player_on_ground = False

    if player.colliderect(goal):
        import win

    if player.colliderect(enemy) and small:
        lives -= 1
        player_size = 40
        player_x = 100
        player_y = 270     
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        screen.blit(player_rect, player)
        if lives == 0:
            import end  
    elif player.colliderect(enemy) and not small:
        lives -= 1
        player_size = 40
        player_x = 100
        player_y = 270     
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        screen.blit(player_rect, player)
        if lives == 0:
            import end

    if player.colliderect(wall):
        if player.x < wall.x:
            player.x = wall.x - player_size
        else:
            player.x = wall.x + wall.width

    enemy.x += enemy_speed * enemy_direction
    if enemy.x <= 0 or enemy.x >= WIDTH - ENEMY_SIZE:
        enemy_direction *= -1

    jumppad.x += jumppad_speed * jumppad_direction
    if jumppad.x <= 370 or jumppad.x >= (jumppad_x + 300):
        jumppad_direction *= -1

    if player.x < 1:
        player.x += push

    elif player.x > 1059:
        player.x -= push

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, GROUND_COLOR, ground)

    pygame.draw.rect(screen, PLATFORM_COLOR, platform_1)
    pygame.draw.rect(screen, PLATFORM_COLOR, platform_2)

    pygame.draw.rect(screen, ENEMY_COLOR, enemy)

    pygame.draw.rect(screen, JUMPPAD_COLOR, jumppad)
    pygame.draw.rect(screen, JUMPPAD_COLOR, jumppad_2)

    pygame.draw.rect(screen, GOAL_COLOR, goal)

    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)

    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (200, 10))

    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(coins_text, (400, 10)

    screen.blit(player_rect, player)

    pygame.draw.rect(screen, (0, 0, 0), wall)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()