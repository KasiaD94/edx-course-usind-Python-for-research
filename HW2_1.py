# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:46:03 2020

@author: Kasia
"""

import numpy
import random

def create_board(): 
    board = numpy.zeros((3,3), dtype = int)
    return(board) 

def place(board, player, position):
    if board[(position)] == 0:
        board[(position)] = player    
    return board
#place(create_board(), 1, (0,0))

def possibilities(board):
    free_place = numpy.where(board<1)
    listOfCoordinates= list(zip(free_place[0], free_place[1]))
    coord_list = []
    for cord in listOfCoordinates:
        coord_list.append(cord)
    return coord_list
#possibilities(place(create_board(), 1, (0,0)))


def random_place(board, player):
    possible_places = possibilities(board)
    curr_location = random.choice(possible_places)
    board[curr_location] = player
    return board

#random_place(place(create_board(), 1, (0,0)), 2)

#board = create_board()
#
#player = 1 
#for i in range(9):
#    random_place(board, player)
#    if player == 1:
#        player = 2
#    elif player == 2:
#        player = 1
        
#print(board)

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x,y] != player:
                win = False
                continue
        if win == True:
            return win
    return win

#row_win(board, player)

def col_win(board, player):
    board2 = numpy.transpose(board)
    win = row_win(board2, player)
    return win
#def col_win(board, player): 
#    for x in range(len(board)): 
#        win = True      
#        for y in range(len(board)): 
#            if board[y][x] != player: 
#                win = False
#                continue
#        if win == True: 
#            return(win) 
#    return(win) 
#print(col_win(board, player))

#board[1,1] = 2

def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x,x] != player:
            win = False
            continue
    
    if board[0,2] == board[1,1] == board[2,0] == player:
        win = True
    return win

#diag_win(board, player=2)

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or 
            col_win(board, player) or 
            diag_win(board, player)):
            winner = player
    if numpy.all(board != 0) and winner == 0:
        winner = -1
    return winner


#print(evaluate(board))
random.seed(1)
results = []

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1,2]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0: 
                break
#    print(board)
    return winner

#print(play_game())
random.seed(1)
def play_strategic_game():
    board = numpy.array([[0,0,0],[0,1,0],[0,0,0]])
    winner = 0
    while winner == 0:
        for player in [2,1]:
            board = random_place(board, player)
            winner = evaluate(board)
            if winner != 0: 
                break
    return winner
#print(play_strategic_game())

for i in range(1000):
    result = play_strategic_game()
    results.append(result)

count = 0
for i in range(1000):
    if results[i] == 1:
        count += 1
print(count)
