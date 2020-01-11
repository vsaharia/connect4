import pygame, sys
from pygame.locals import *
import math
import numpy as np

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)
YELLOW = (255, 255, 0)

BACKGROUND = pygame.display.set_mode((500,900))
game_board = pygame.Rect(0, 250, 500, 400)
font = pygame.font.SysFont("HP Simplified", 45)
font2 = pygame.font.SysFont("Cafeteria-Bold", 100)
player1_text = font.render("Player 1", True, RED)
player2_text = font.render("Player 2", True, YELLOW)
connect4_text = font2.render("Connect Four", True, WHITE)
draw_text = font2.render("IT'S A DRAW!", True, WHITE)
p1_win = font2.render("P1 WINS!", True, RED)
p2_win = font2.render("P2 WINS!", True, YELLOW)

turn = 0
game_over = False

RADIUS = 29
Y_DIFF = 64
X_DIFF = 68
HEIGHT = 610
ROWS = 6
COLUMNS = 7

board = np.zeros((6,7))

def col_pos(x):
    return {
        0: 50+X_DIFF*0,
        1: 50+X_DIFF*1,
        2: 50+X_DIFF*2,
        3: 50+X_DIFF*3,
        4: 50+X_DIFF*4,
        5: 50+X_DIFF*5,
        6: 50+X_DIFF*6,
    }[x]  

def check_draw():

	draw_count = 0

	for c in range(0, COLUMNS):
		for r in range(0, ROWS):
			if board[r][c]==1 or board[r][c]==2:
				draw_count+=1
	if draw_count==42:
		pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
		BACKGROUND.blit(draw_text, (80, 100))
		return True		


def check_win(player):

	for c in range(COLUMNS-3):
		for r in range(ROWS):
			if board[r][c]==player and board[r][c+1]==player and board[r][c+2]==player and board[r][c+3]==player:
				pygame.draw.line(BACKGROUND, BLACK, (col_pos(c), HEIGHT-r*Y_DIFF), (col_pos(c+3), HEIGHT-r*Y_DIFF), 10)

				if player == 1:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p1_win, (120, 100))
					return True


				elif player == 2:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p2_win, (120, 100))
					return True	



	for c in range(COLUMNS):
		for r in range(ROWS-3):
			if board[r][c]==player and board[r+1][c]==player and board[r+2][c]==player and board[r+3][c]==player:
				pygame.draw.line(BACKGROUND, BLACK, (col_pos(c), HEIGHT-r*Y_DIFF), (col_pos(c), HEIGHT-(r+3)*Y_DIFF), 10)

				if player == 1:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p1_win, (120, 100))
					return True

				elif player == 2:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p2_win, (120, 100))
					return True

	for c in range(COLUMNS-3):
		for r in range(ROWS-3):
			if board[r][c]==player and board[r+1][c+1]==player and board[r+2][c+2]==player and board[r+3][c+3]==player:
				pygame.draw.line(BACKGROUND, BLACK, (col_pos(c), HEIGHT-r*Y_DIFF), (col_pos(c+3), HEIGHT-(r+3)*Y_DIFF), 10)

				if player == 1:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p1_win, (120, 100))
					return True
				elif player == 2:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p2_win, (120, 100))
					return True

	for c in range(COLUMNS-3):
		for r in range(3, ROWS):
			if board[r][c]==player and board[r-1][c+1]==player and board[r-2][c+2]==player and board[r-3][c+3]==player:
				pygame.draw.line(BACKGROUND, BLACK, (col_pos(c), HEIGHT-r*Y_DIFF), (col_pos(c+3), HEIGHT-(r-3)*Y_DIFF), 10)	

				if player == 1:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p1_win, (120, 100))
					return True
				elif player == 2:
					pygame.draw.rect(BACKGROUND, BLACK, (0, 70, 500, 150))
					BACKGROUND.blit(p2_win, (120, 100))
					return True		
					
def drop_piece(turn, xpos):

	piece_xpos = int(math.floor(xpos/X_DIFF))
	if piece_xpos == 7:
		piece_xpos = 6
	b = check_open_row(piece_xpos)

	if turn == 0:
		board[b][piece_xpos] = 1
	else: 
		board[b][piece_xpos] = 2
	print(np.flip(board, 0))

def draw_board():
	for c in range(0,COLUMNS):
		for r in range(0,ROWS):
			if board[r][c]==1:
				pygame.draw.circle(BACKGROUND, RED, (col_pos(c), HEIGHT-r*Y_DIFF), RADIUS)
			elif board[r][c]==2:
				pygame.draw.circle(BACKGROUND, YELLOW, (col_pos(c), HEIGHT-r*Y_DIFF), RADIUS)
	
def check_open_row(col):
	for r in range(ROWS):
		if board[r][col]==0:
			return r		

def can_be_placed(col):
	return board[ROWS-1][col] == 0		

def game_setup():

	pygame.display.set_caption('Connect 4!')
	pygame.draw.rect(BACKGROUND, BLUE, game_board)
	
	for x in range(0, 7):
		for y in range(0, 6):
			pygame.draw.circle(BACKGROUND, WHITE, (50+x*X_DIFF, 290+y*Y_DIFF), RADIUS)

	BACKGROUND.blit(player1_text, (20,10))
	BACKGROUND.blit(player2_text, (255, 10))
	BACKGROUND.blit(connect4_text, (60, 60))
	pygame.draw.circle(BACKGROUND, RED, (210, 40), RADIUS)
	pygame.draw.circle(BACKGROUND, YELLOW, (450, 40), RADIUS)

game_setup()
pygame.display.update()

while not game_over:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()	
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(BACKGROUND, BLACK, (0, 170, 500, 60))
			x_pos = event.pos[0]
			if turn == 0:
				pygame.draw.circle(BACKGROUND, RED, (x_pos, 200), RADIUS)
			else:
				pygame.draw.circle(BACKGROUND, YELLOW, (x_pos, 200), RADIUS)

		pygame.display.update()	
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_xpos = event.pos[0]
			col = int(math.floor(mouse_xpos/X_DIFF))
			if col == 7:
				col = 6
			if can_be_placed(col):
				pygame.mixer.music.load('connect4_trimmed.mp3')
				pygame.mixer.music.play()
				drop_piece(turn, mouse_xpos)
				if turn == 0:
					if check_draw():
						pygame.display.update()
						game_over=True
					if(check_win(1)):
						pygame.display.update()
						game_over=True
					turn = 1
				else:
					if check_draw():
						pygame.display.update()
						game_over=True
					if(check_win(2)):
						pygame.display.update()
						game_over=True
					turn = 0			
		draw_board()

		if game_over:
			pygame.draw.rect(BACKGROUND, BLACK, (0, 200, 500, 30))
			pygame.display.update()
			pygame.time.wait(3000)					

	pygame.display.update()	
