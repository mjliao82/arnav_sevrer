import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1100, 600
PLAYER_SIZE = 40
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
GOAL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
PLATFORM_COLOR = (0, 0, 255)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
JUMP_STRENGTH = -12
MOVE_SPEED = 4.5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
lives = 3
coins = 0

#Create the PLayer
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

platform_2_y = 200
platform_2_x = 800
platform_2_width = 200
platform_2_height = 20
platform_2 = pygame.Rect(platform_2_x, platform_2_y, platform_2_width, platform_2_height)

# Create a goal
goal_x = 400
goal_y = 5
goal_width = 70
goal_height = 100
goal = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

# Create coins
coin_size = 40
coin_img = pygame.image.load("coin.jpg").convert()
coin_1 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_1 = coin_1.get_rect(topleft=(700, 220))
coin_2 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_2 = coin_2.get_rect(topleft=(150, 200))
coin_3 = pygame.transform.scale(coin_img, (coin_size, coin_size))
coin_rect_3 = coin_3.get_rect(topleft=(500, 250))




# Clock for controlling frame rate
clock = pygame.time.Clock()
push = 5

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
    if keys[pygame.K_0]:
        import end
    if keys[pygame.K_2]:
        import second
    if keys[pygame.K_3]:
        import third
    if keys[pygame.K_4]:
        import fourth
    if keys[pygame.K_5]:
        import fifth
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_a]:
        player2.x -= MOVE_SPEED
    if keys[pygame.K_d]:
        player2.x += MOVE_SPEED
    if keys[pygame.K_SPACE]:
        import instructions
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

     # Jump control (using the up arrow key)
    if keys[pygame.K_UP] and player_on_ground:
        player_velocity = JUMP_STRENGTH
        player_on_ground = False

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

    if (player.y < platform_2_y and player.y > (platform_2_y - 40)) and (player.x > platform_2_x and player.x < platform_2_x + 190):
       player.y = platform_2.y - PLAYER_SIZE
       player_on_ground = True
       player_velocity = 0

    #Check for second player collisions with the platform
    if (player2.y < platform_1_y and player2.y > (platform_1_y - 40)) and (player2.x > platform_1_x and player2.x < platform_1_x + 190):
       player2.y = platform_1.y - PLAYER_SIZE
       player2_on_ground = True
       player2_velocity = 0

    if (player2.y < platform_2_y and player2.y > (platform_2_y - 40)) and (player2.x > platform_2_x and player2.x < platform_2_x + 190):
       player2.y = platform_2.y - PLAYER_SIZE
       player2_on_ground = True
       player2_velocity = 0

    if player.x < 1:
        player.x += push

    elif player.x > 1059:
        player.x -= push

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
        if player.colliderect(goal) and player2.colliderect(goal):
            import next_2



    if player2.x < 1:
        player2.x += push

    elif player2.x > 1059:
        player2.x -= push

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
    pygame.draw.rect(screen, PLATFORM_COLOR, platform_2)

    # Draw the goal
    pygame.draw.rect(screen, GOAL_COLOR, goal)

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # Draw the second player
    pygame.draw.rect(screen, PLAYER_COLOR, player2)

    #Display lives
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    screen.blit(lives_text, (10, 10))

    #Display coin_score
    coins_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
    screen.blit(coins_text, (910, 10))

    #screen.blit(resizer, resizer_rect)

    #Display coins
    screen.blit(coin_1, coin_rect_1)
    screen.blit(coin_2, coin_rect_2)
    screen.blit(coin_3, coin_rect_3)

    # Draw the player
    screen.blit(player_rect, player)
    # Draw the second player
    screen.blit(player2_rect, player2)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
