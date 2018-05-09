#!/usr/bin/env python3

print("Battleship")

empty = '  O  '

rows = 8
cols = 8
board = []

for r in range(rows):
    row = []
    for c in range(cols):
        row.append(empty)
    board.append(row)

def print_cell(cell):
    print(cell, end='')

def print_header(columns):
    # row labels offset
    left_margin = '   '
    header_text = ''
    for i in range(columns):
        header_text += empty.replace('O', str(i))
    header_separator = '-' * len(header_text)
    print(f'{left_margin}{header_text}')
    print(f'{left_margin}{header_separator}')

def print_row(row):
    for cell in row:
        print_cell(cell)
    print('\n')

def print_board(board):
    print_header(len(board[0]))
    for index, row in enumerate(board):
        print(f'{index} |', end='')
        print_row(row)

print_board(board)
