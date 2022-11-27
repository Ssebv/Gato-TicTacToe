import sys
import pygame #Graphics
import numpy as np

# print (pygame.ver)

from constants import *

# PYGAME SETUP
pygame.init() #Initialize pygame
screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) #Set screen size
pygame.display.set_caption("Tic Tac Toe AI") #Set window title
screen.fill( BG_COLOR ) #Fill screen with color

class Board:
    
    def __init__(self):
        self.squeres = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squeres
        self.marked_sqrs = 0 
        
    def final_state(self):
        '''
         @ return 0 if there is no win yet
         @ return 1 if player 1 wins
         @ return 2 if player 2 wins
        '''
        
        # vertical wins
        for col in range(COLS):
            if self.squeres[0][col] == self.squeres[1][col] == self.squeres[2][col] != 0:
                return self.squeres[0][col]
        
        # horizontal wins
        for row in range(ROWS):
            if self.squeres[row][0] == self.squeres[row][1] == self.squeres[row][2] != 0:
                return self.squeres[row][0]
        
        # descending diagonal wins
        
        if self.squeres[0][0] == self.squeres[1][1] == self.squeres[2][2] != 0:
            return self.squeres[1][1]

        # ascending diagonal wins
        
        if self.squeres[2][0] == self.squeres[1][1] == self.squeres[0][2] != 0:
            return self.squeres[1][1]
        # no win yet
        return 0
                  
    def mark_sqr(self, row, col, player):
        self.squeres[row, col] = player
        self.marked_sqrs += 1
        
    def empty_sqr(self, row, col):
        return self.squeres[row, col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )
        
        return empty_sqrs            
        pass
    
    def infull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0

class Game:
    
    def __init__(self):
        self.board = Board()
        # self.ia = AI()
        self.player = 1 # 1 = X, 2 = O
        self.gamemode = 'PVP'
        self.running = True 
        self.show_line()
    
    def show_line(self):
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
        
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH,  SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)
    
    def draw_fig(self, row, col):
         if self.player == 1:
             #draw X
             
             # desc line 
             start_desc = (col * SQSIZE + OFF_SET , row * SQSIZE + OFF_SET) 
             end_desc = (col * SQSIZE + SQSIZE - OFF_SET, row * SQSIZE + SQSIZE - OFF_SET)
             pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
             
             # asc line
             start_desc = (col * SQSIZE + OFF_SET , row * SQSIZE + SQSIZE - OFF_SET) 
             end_desc = (col * SQSIZE + SQSIZE - OFF_SET, row * SQSIZE + OFF_SET)
             pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
             
             
             pass
         elif self.player == 2:
             #draw 0
             center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
             pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)
        
    def next_turn(self):
        self.player = self.player % 2 + 1
           
def main():
    
    # Object
    
    game = Game()
    board = game.board 
    
    # Main Loop
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos #Get mouse position
                row = pos[1] // SQSIZE #Get row
                col = pos[0] // SQSIZE #Get column 
                
                if board.empty_sqr(row, col):
                    board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.next_turn()
                    print(board.squeres)
                    
               
                
        
        pygame.display.update()


main()