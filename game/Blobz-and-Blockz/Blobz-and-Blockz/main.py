import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 1100, 600
PLAYER_SIZE = 40
PLAYER_COLOR = (255, 0, 0)
GROUND_COLOR = (0, 255, 0)
BG_COLOR = (255, 255, 255)
GRAVITY = 0.5
JUMP_STRENGTH = -12
MOVE_SPEED = 4.5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Create the player character
player_x = 350
player_y = 100
player_velocity = 0
player_on_ground = False
player_img = pygame.image.load("super_super_drippy.jpg").convert()
player_rect = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
player = player_rect.get_rect(topleft=(player_x, player_y))

# Create the ground
ground_x = 0
ground_y = 400
ground_height = 20
ground = pygame.Rect(ground_x, ground_y, WIDTH, ground_height)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    font_1 = pygame.font.Font(None, 60)
    font_2 = pygame.font.Font(None, 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += MOVE_SPEED
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
        

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw the ground
    pygame.draw.rect(screen, GROUND_COLOR, ground)

    # Draw the player
    screen.blit(player_rect, player)

    # Display game title
    text_1 = "WELCOME TO"
    text_2 = "BLOBZ AND BLOCKZ"
    text_3 = "Press Space to Play"
    title_text_1 = font_1.render(text_1, True, (0, 0, 0))
    title_text_2 = font_2.render(text_2, True, (0, 0, 0))
    title_text_3 = font_1.render(text_3, True, (0, 0, 0))
    screen.blit(title_text_1, (WIDTH//2 - title_text_1.get_width()//2, 10))
    screen.blit(title_text_2, (WIDTH//2 - title_text_2.get_width()//2, 50))
    screen.blit(title_text_3, (WIDTH//2 - title_text_3.get_width()//2, 110))

    # Update the display
    pygame.display.update()
 
    # Control the frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()