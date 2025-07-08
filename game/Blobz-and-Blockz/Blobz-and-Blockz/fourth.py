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
orb_color = (117, 199, 173)
ENEMY_COLOR = (0, 0, 0)
SPIKE_COLOR = (0, 0, 0)
player_size = 40
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
PLATFORM_COLOR = (0, 0, 255)
JUMPPAD_COLOR = (255, 217, 3)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
jump_strength = -12
MOVE_SPEED = 4.5
EXTRA_JUMP = -18
LITTLE_JUMP = -4

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
lives = 3
coins = 0

# Create the player character
player_x = 50
player_y = 360
player_size = 40
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect = pygame.transform.scale(player_img, (player_size, player_size))
player = player_rect.get_rect(topleft=(player_x, player_y))
jumps_remaining = 3  # Number of jumps the player can perform

# Create the wall
wall_x = 900
wall_y = 70
wall_width = 20
wall_height = 330
wall = pygame.Rect(wall_x, wall_y, wall_width, wall_height)

# Create the ground
ground_x = 0
ground_y = 400
ground_height = 20
ground_width = WIDTH - (WIDTH - wall_x) + wall_width
ground = pygame.Rect(ground_x, ground_y, ground_width, ground_height)

ground_2_x = 0
ground_2_y = 550
ground_2_height = 20
ground_2_width = WIDTH
ground_2 = pygame.Rect(ground_2_x, ground_2_y, ground_2_width, ground_2_height)

#Create a spike
spike_1_x = 400
spike_1_y = 515
spike_1_width = 25
spike_1_height = 35
spike_1 = pygame.Rect(spike_1_x, spike_1_y, spike_1_width, spike_1_height)

spike_2_x = 600
spike_2_y = 515
spike_2_width = 25
spike_2_height = 35
spike_2 = pygame.Rect(spike_2_x, spike_2_y, spike_2_width, spike_2_height)

#Create an enemy
enemy_x = 600
enemy_y = 360
enemy_speed = 10
enemy_direction = 1
enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)

enemy_2_x = 400
enemy_2_y = 360
enemy_2_speed = 7
enemy_2_direction = 1
enemy_2 = pygame.Rect(enemy_2_x, enemy_2_y, ENEMY_SIZE, ENEMY_SIZE)

enemy_3_x = 200
enemy_3_y = 360
enemy_3_speed = 8
enemy_3_direction = 1
enemy_3 = pygame.Rect(enemy_3_x, enemy_3_y, ENEMY_SIZE, ENEMY_SIZE)



# Create a goal
goal_x = 150
goal_y = 425
goal_width = 70
goal_height = 100
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

# Create the orb
orb_x = 1000
orb_y = 470
orb_size = 20
orb = pygame.Rect(orb_x, orb_y, orb_size, orb_size)


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
small_jump = False
flicker = False

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

    # Check for first jump (Up arrow)
    if keys[pygame.K_UP] and player_on_ground and jumps_remaining == 3:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1

    # Check for second jump (Spacebar)
    if keys[pygame.K_SPACE] and not player_on_ground and jumps_remaining == 2:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1

    # Check for third jump (F key)
    if keys[pygame.K_f] and not player_on_ground and jumps_remaining == 1:
        player_velocity = jump_strength
        player_on_ground = False
        jumps_remaining -= 1

    if player.colliderect(ground):
        player.y = ground.y - player_size
        player_on_ground = True
        player_velocity = 0
        jumps_remaining = 3  # Reset jumps when landing on the ground

    if player.colliderect(ground_2):
        player.y = ground_2.y - player_size
        player_on_ground = True
        player_velocity = 0
        jumps_remaining = 3  # Reset jumps when landing on the ground

    if player.colliderect(spike_1) or player.colliderect(spike_2):
        small_jump = False
        lives -= 1
        player_x = 150
        player_y = 360
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        if lives == 0:
            import end

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

    if player.colliderect(enemy):
        lives -= 1
        player_size = 40
        player_x = 100
        player_y = 360
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        screen.blit(player_rect, player)
        if lives == 0:
            import end
    elif player.colliderect(enemy_2):
        lives -= 1
        player_size = 40
        player_x = 100
        player_y = 360
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        screen.blit(player_rect, player)
        if lives == 0:
            import end

    elif player.colliderect(enemy_3):
        lives -= 1
        player_size = 40
        player_x = 100
        player_y = 360
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        screen.blit(player_rect, player)
        if lives == 0:
            import end

    if player.colliderect(orb) and not flicker:
        small_jump = not small_jump
        flicker = True
    if not player.colliderect(orb):
        flicker = False
    if small_jump:
        jump_strength = -9
        orb_color = (207, 53, 39)
        jumps_remaining = 3

    elif not small_jump:
        jump_strength = -12
        orb_color = (117, 199, 173)

    if player.colliderect(wall):
        if player.x < wall.x:
            player.x = wall.x - player_size
        else:
            player.x = wall.x + wall.width

    enemy.y += enemy_speed * enemy_direction
    if enemy.y <= 0 or enemy.y >= (HEIGHT - 230):
        enemy_direction *= -1

    enemy_2.y += enemy_2_speed * enemy_2_direction
    if enemy_2.y <= 0 or enemy_2.y >= (HEIGHT - 230):
        enemy_2_direction *= -1

    enemy_3.y += enemy_3_speed * enemy_3_direction
    if enemy_3.y <= 0 or enemy_3.y >= (HEIGHT - 230):
        enemy_3_direction *= -1
        

    if player.x < 1:
        player.x += push

    elif player.x > 1059:
        player.x -= push

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, GROUND_COLOR, ground)
    pygame.draw.rect(screen, GROUND_COLOR, ground_2)

    pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_2)
    pygame.draw.rect(screen, ENEMY_COLOR, enemy_3)

    pygame.draw.circle(screen, orb_color, (orb_x, orb_y), orb_size)


    #Draw the 1st spike
    pygame.draw.rect(screen, SPIKE_COLOR, spike_1)

    #Draw the 2nd spike
    pygame.draw.rect(screen, SPIKE_COLOR, spike_2)

    pygame.draw.rect(screen, GOAL_COLOR, goal)

    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)

    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (200, 10))

    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(coins_text, (400, 10))

    screen.blit(player_rect, player)

    pygame.draw.rect(screen, (0, 0, 0), wall)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
