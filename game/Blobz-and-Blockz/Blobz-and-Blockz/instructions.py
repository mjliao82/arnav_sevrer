import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Win")

font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
text = font.render("INSTRUCTIONS:", True, (0, 0, 0))

lines = [
    "You have 3 lives. You need to collect 3 coins. If you are on a",
    "platform, you can slide off of it, and there will be an invisible",
    "path. Anything colored black (except for the walls) is an enemy and will make you lose one of",
    "your lives. After you collect all 3 coins, the exit will be open",
    "You have to reach an exit which changes colors every time you play",
    "the game. Now play Blobz and Blockz."
]

text_lines = [small_font.render('', True, (0, 0, 0)) for _ in lines]
text_space = font.render("Press Enter to Continue", True, (0, 0, 0))

running = True
counter = 0
line_counter = 0
char_counter = 0
text_finished = False

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_RETURN]:
        import first  # Consider moving the import statement outside the main loop

    if not text_finished:
        if counter % 0.5 == 0:  # Adjust the timing to control the typing speed
            if line_counter < len(lines):
                if char_counter < len(lines[line_counter]):
                    text_lines[line_counter] = small_font.render(
                        lines[line_counter][:char_counter+1], True, (0, 0, 0)
                    )
                    char_counter += 1
                else:
                    line_counter += 1
                    char_counter = 0
                    if line_counter == len(lines):
                        text_finished = True

        counter += 1

    screen.fill((255, 255, 255))
    screen.blit(text, (50, 10))
    for i, text_line in enumerate(text_lines):
        screen.blit(text_line, (20, 80 + i * 50))
    if text_finished:
        screen.blit(text_space, (50, 430))
    pygame.display.flip()
    clock.tick(30)  # Adjust the frame rate as per your requirement

pygame.quit()
sys.exit()