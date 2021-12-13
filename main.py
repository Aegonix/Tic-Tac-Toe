import pygame
import os

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 601, 601
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

BACKGROUND_IMG = pygame.image.load(
    os.path.join("Assets", "background.jpg")).convert_alpha()
X_IMAGE = pygame.image.load(
    os.path.join("Assets", "x.png")).convert_alpha()
O_IMAGE = pygame.image.load(
    os.path.join("Assets", "o.png")).convert_alpha()

BLACK = (0, 0, 0)

def draw_win(win):
    win.blit(BACKGROUND_IMG, (0, 0))

def main():
    print(BACKGROUND_IMG.get_size())
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.blit(BACKGROUND_IMG, (0, 0))
    
if __name__ == "__main__":
    main()