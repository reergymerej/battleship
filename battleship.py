#!/usr/bin/env python3

print("Battleship")

empty = '  .  '
ship =  '  O  '
miss =  '  *  '
hit =   '  #  '

class Cell:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def print(self):
        print(self.state, end='')

class Row:
    def __init__(self):
        self.cells = []

    def append(self, cell_state):
        self.cells.append(Cell(cell_state))

    def set_cell(self, cell, state):
        self.cells[cell].set_state(state)

    def print(self):
        for cell in self.cells:
            cell.print()
        print('\n')

class Header:
    def __init__(self, columns):
        header_text = ''
        for i in range(columns):
            header_text += f'  {i}  '
        header_separator = '-' * len(header_text)
        self.header_text = header_text
        self.header_separator = header_separator

    def print(self):
        # row labels offset
        left_margin = '   '
        print(f'{left_margin}{self.header_text}')
        print(f'{left_margin}{self.header_separator}')

class Board:
    def __init__(self, rows, cols):
        self.row_count = rows
        self.col_count = cols
        self.rows = self.build_rows(rows, cols)
        self.header = Header(cols)

    def build_rows(self, row_count, col_count):
        rows = []
        for r in range(row_count):
            row = Row()
            for c in range(col_count):
                row.append(empty)
            rows.append(row)
        return rows

    def set_cell(self, col, row, state):
        self.rows[row].set_cell(col, state)

    def print(self):
        self.header.print()
        for index, row in enumerate(self.rows):
            print(f'{index} |', end='')
            row.print()

rows = 8
cols = 8
board = Board(rows, cols)

board.set_cell(3, 2, ship)
board.set_cell(3, 3, ship)
board.set_cell(2, 4, miss)
board.set_cell(3, 4, hit)
board.set_cell(3, 5, ship)
board.set_cell(4, 4, miss)

board.print()
