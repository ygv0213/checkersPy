import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 0)
GREY = (128, 128, 128)

#IMAGES
CROWN = pygame.transform.scale(pygame.image.load("assets/crowns.png"), (30, 30))
