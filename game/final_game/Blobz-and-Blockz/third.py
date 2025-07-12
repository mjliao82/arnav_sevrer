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
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
ENEMY_COLOR = (0, 0, 0)
JUMPPAD_COLOR = (255, 217, 3)
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
PLATFORM_COLOR = (0, 0, 255)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
JUMP_STRENGTH = -12
MOVE_SPEED = 4.5
EXTRA_JUMP = -18

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

one_player_done = False

player_gone = False
player2_gone = False


#Create the Player
player_x = 350
player_y = 100
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
player = player_rect.get_rect(topleft=(player_x, player_y))

# Creates second player
player2_x = 350
player2_y = 100
player2_velocity = 0
player2_on_ground = False
player2_img = pygame.image.load("image.jpg").convert()
player2_rect = pygame.transform.scale(player2_img, (PLAYER_SIZE, PLAYER_SIZE))
player2 = player2_rect.get_rect(topleft=(player2_x, player2_y))

# Create the ground
ground_x = 0
ground_y = 400
ground_height = 20
ground = pygame.Rect(ground_x, ground_y, WIDTH, ground_height)

# Create a platform
platform_1_y = 300
platform_1_x = 100
platform_1_width = 200
platform_1_height = 20
platform_1 = pygame.Rect(platform_1_x, platform_1_y, platform_1_width, platform_1_height)


# Create a goal
goal_x = 900
goal_y = 5
goal_width = 70
goal_height = 100
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

#Create an enemy
enemy_x = 500
enemy_y = 360
enemy_speed = 7
enemy_direction = 1
enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)

#Create a jump pad
jumppad_x = 500
jumppad_y = 380
jumppad_width = 150
jumppad_height = 20
jumppad_speed = 3
jumppad_direction = 1
jumppad = pygame.Rect(jumppad_x, jumppad_y, jumppad_width, jumppad_height)

#Create coins
coin_size = 40
coin_img = pygame.image.load("coin.jpg").convert()
coin_1 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_1 = coin_1.get_rect(topleft=(800, 150))
coin_2 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_2 = coin_2.get_rect(topleft=(300, 350))
coin_3 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_3 = coin_3.get_rect(topleft=(450, 100))

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

    # Handle player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += MOVE_SPEED
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_a]:
        player2.x -= MOVE_SPEED
    if keys[pygame.K_d]:
        player2.x += MOVE_SPEED
    if keys[pygame.K_SPACE]:
        import instructions

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
        
    # Apply gravity
    if not player2_on_ground:
        player2_velocity += GRAVITY

    # Update player's vertical position
    player2.y += player2_velocity

    # Check for collisions with the ground
    if player2.colliderect(ground):
        player2.y = ground.y - PLAYER_SIZE
        player2_on_ground = True
        player2_velocity = 0

    # Check for collisions with the platform
    if (player.y < platform_1_y and player.y > (platform_1_y - 40)) and (player.x > platform_1_x and player.x < platform_1_x + 190):
       player.y = platform_1.y - PLAYER_SIZE
       player_on_ground = True
       player_velocity = 0

    if player.x < 1:
        player.x += push

    elif player.x > 1059:
        player.x -= push
        
    # Check for collisions with the platform
    if (player2.y < platform_1_y and player2.y > (platform_1_y - 40)) and (player2.x > platform_1_x and player2.x < platform_1_x + 190):
       player2.y = platform_1.y - PLAYER_SIZE
       player2_on_ground = True
       player2_velocity = 0

    if player2.x < 1:
        player2.x += push

    elif player2.x > 1059:
        player2.x -= push

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
        
    # Check for collisions with coins
    if player2.colliderect(coin_rect_1):
        coins += 1
        coin_rect_1.x = 2000
    if player2.colliderect(coin_rect_2):
        coins += 1
        coin_rect_2.x = 2000
    if player2.colliderect(coin_rect_3):
        coins += 1
        coin_rect_3.x = 2000

    if coins == 3:
        GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if player.colliderect(goal) and not player_gone:
            if one_player_done:
                import next_4
            else:
                one_player_done = True
                player_gone = True
                player.x = -1000  # move offscreen
                player.y = -1000

        if player2.colliderect(goal) and not player2_gone:
            if one_player_done:
                import next_4
            else:
                one_player_done = True
                player2_gone = True
                player2.x = -1000  # move offscreen
                player2.y = -1000


    if player.colliderect(jumppad):
        player_velocity = EXTRA_JUMP
        player_on_ground = False

    if player.colliderect(enemy):
        lives -= 1
        player_x = 150
        player_y = 270
        player = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
        if lives == 0:
            import end
            
    if player2.colliderect(jumppad):
        player2_velocity = EXTRA_JUMP
        player2_on_ground = False

    if player2.colliderect(enemy):
        lives -= 1
        player2_x = 150
        player2_y = 270
        player2 = pygame.Rect(player2_x, player2_y, PLAYER_SIZE, PLAYER_SIZE)
        if lives == 0:
            import end
        
    enemy.x += enemy_speed * enemy_direction
    if enemy.x <= 0 or enemy.x >= WIDTH - ENEMY_SIZE:
        enemy_direction *= -1

    jumppad.x += jumppad_speed * jumppad_direction
    if jumppad.x <= (jumppad_x - 200) or jumppad.x >= (jumppad_x + 450):
        jumppad_direction *= -1
    

    # Jump control (using the up arrow key)
    if keys[pygame.K_UP] and player_on_ground:
        player_velocity = JUMP_STRENGTH
        player_on_ground = False
        
    # Jump control second (using the up arrow key)
    if keys[pygame.K_w] and player2_on_ground:
        player2_velocity = JUMP_STRENGTH
        player2_on_ground = False
        
    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the ground
    pygame.draw.rect(screen, GROUND_COLOR, ground)

    # Draw the platform
    pygame.draw.rect(screen, PLATFORM_COLOR, platform_1)

    #Display coins
    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)
    
    # Draw the goal
    pygame.draw.rect(screen, GOAL_COLOR, goal)

    # Draw the player
    screen.blit(player_rect, player)
    
    # Draw the second player
    screen.blit(player2_rect, player2)

    # Draw the enemy
    pygame.draw.rect(screen, ENEMY_COLOR, enemy)

    # Draw a jumppad
    pygame.draw.rect(screen, JUMPPAD_COLOR, jumppad)

    #Display lives
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (10, 10))

    #Display coin_score
    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(coins_text, (910, 10))
   

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
