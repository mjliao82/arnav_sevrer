import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Win")

font = pygame.font.Font(None, 100)
text = font.render("YOU WIN! GOOD JOB!", True, (0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    screen.fill((255, 255, 255))
    screen.blit(text, (WIDTH/5, HEIGHT/3))
    pygame.display.flip()

pygame.quit()
sys.exit()