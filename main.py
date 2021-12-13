import pygame
import os
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 601, 601
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
pygame.display.set_icon(pygame.image.load("Assets/icon.png").convert_alpha())

BACKGROUND_IMG = pygame.image.load("Assets/background.png").convert_alpha()
X_IMAGE = pygame.transform.smoothscale(
    pygame.image.load("Assets/x.png"), (160, 160)).convert_alpha()
O_IMAGE = pygame.transform.smoothscale(
    pygame.image.load("Assets/o.png"), (160, 160)).convert_alpha()
pygame.mixer.music.load("Assets/error.mp3")

X = "X"
O = "O"
BLACK = (0, 0, 0)
board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
IMAGES = {
    X : X_IMAGE,
    O : O_IMAGE
}
BLIT_COORDS = {
    1 : (35, 30),
    2 : (220, 30),
    3 : (405, 30),
    4 : (35, 220),
    5 : (220, 220),
    6 : (405, 220),
    7 : (35, 410),
    8 : (220, 410),
    9 : (405, 410)
}
font_path = pygame.font.match_font("Fira Code")
if font_path:
    font = pygame.font.Font(font_path, 40)
else:
    font = pygame.font.Font(pygame.font.get_default_font(), 40)

def check_winner(board):
    if board[1] == board[2] and board[2] == board[3]:
        return board[1]
    elif board[1] == board[4] and board[4] == board[7]:
        return board[1]
    elif board[1] == board[5] and board[5] == board[9]:
        return board[1]
    elif board[2] == board[5] and board[5] == board[8]:
        return board[2]
    elif board[3] == board[6] and board[6] == board[9]:
        return board[3]
    elif board[3] == board[5] and board[5] == board[7]:
        return board[3]
    elif board[9] == board[8] and board[8] == board[7]:
        return board[9]
    elif board.count(0) == 1:
        return "Tie"

def update_board(pos, board, turn):
    if (pos[0] >= 20 and pos[0] <= 210) and (pos[1] >= 20 and pos[1] <= 210):
        if board[1] == 0: board[1] = turn
        else:
            pygame.mixer.music.play() 
            return False
    elif (pos[0] >= 210 and pos[0] <= 390) and (pos[1] >= 20 and pos[1] <= 210):
        if board[2] == 0: board[2] = turn
        else: 
            pygame.mixer.music.play()
            return False
    elif (pos[0] >= 390 and pos[0] <= 585) and (pos[1] >= 20 and pos[1] <= 210):
        if board[3] == 0: board[3] = turn
        else:
            pygame.mixer.music.play() 
            return False
    elif (pos[0] >= 20 and pos[0] <= 210) and (pos[1] >= 210 and pos[1] <= 390):
        if board[4] == 0: board[4] = turn
        else:
            pygame.mixer.music.play() 
            return False
    elif (pos[0] >= 210 and pos[0] <= 390) and (pos[1] >= 210 and pos[1] <= 390):
        if board[5] == 0: board[5] = turn
        else:
            pygame.mixer.music.play() 
            return False
    elif (pos[0] >= 390 and pos[0] <= 585) and (pos[1] >= 210 and pos[1] <= 390):
        if board[6] == 0: board[6] = turn
        else: 
            pygame.mixer.music.play()
            return False
    elif (pos[0] >= 20 and pos[0] <= 210) and (pos[1] >= 210 and pos[1] <= 585):
        if board[7] == 0: board[7] = turn
        else: 
            pygame.mixer.music.play()
            return False
    elif (pos[0] >= 210 and pos[0] <= 390) and (pos[1] >= 390 and pos[1] <= 585):
        if board[8] == 0: board[8] = turn
        else: 
            pygame.mixer.music.play()
            return False
    elif (pos[0] >= 390 and pos[0] <=585) and (pos[1] >= 390 and pos[1] <= 585):
        if board[9] == 0: board[9] = turn
        else: 
            pygame.mixer.music.play()
            return False
    else:
        pygame.mixer.music.play()
    
    return True

def draw_win(win):
    win.blit(BACKGROUND_IMG, (0, 0))
    for i, val in enumerate(board):
        if val != 0:
            win.blit(IMAGES[val], BLIT_COORDS[i])

def main():
    global board
    clock = pygame.time.Clock()
    run = True
    turn = X
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if turn == X:
                    if update_board(pos, board, X):
                        turn = O
                else:
                    if update_board(pos, board, O):
                        turn = X
        draw_win(WIN)
        pygame.display.flip()
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                TIE_TEXT = font.render(f"Game Over, It was a Tie!", True, BLACK)
                WIN.blit(TIE_TEXT, (300 - TIE_TEXT.get_size()[0]//2, 300 - TIE_TEXT.get_size()[1]//2))
            else:
                WINNER_TEXT = font.render(f"Game Over, {winner} won!", True, BLACK)
                WIN.blit(WINNER_TEXT, (300 - WINNER_TEXT.get_size()[0]//2, 300 - WINNER_TEXT.get_size()[1]//2))
            pygame.display.flip()
            time.sleep(1)
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
if __name__ == "__main__":
    main()