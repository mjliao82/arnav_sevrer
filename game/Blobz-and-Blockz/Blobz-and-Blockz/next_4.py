import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level Up")

font = pygame.font.Font(None, 100)
text1 = font.render("Level Up!", True, (0, 0, 0))
text2 = font.render("Level 4 Unlocked", True, (0, 0, 0))
text3 = font.render("Press Enter to Continue", True, (0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                import fourth

    screen.fill((255, 255, 255))
    text1_pos = text1.get_rect(center=(WIDTH/2, HEIGHT/3))
    text2_pos = text2.get_rect(center=(WIDTH/2, HEIGHT/2))
    text3_pos = text3.get_rect(center=(WIDTH/2, 2*HEIGHT/3))
    screen.blit(text1, text1_pos)
    screen.blit(text2, text2_pos)
    screen.blit(text3, text3_pos)
    pygame.display.flip()

pygame.quit()
sys.exit()
