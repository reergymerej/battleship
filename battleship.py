#!/usr/bin/env python3
import random

print("\nBattleship\n\n")

EMPTY = '  .  '
SHIP =  '  O  '
MISS =  '  *  '
HIT =   '  X  '

class Cell:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def print(self):
        print(self.state, end='')

    def shoot(self):
        if self.state == SHIP:
            self.state = HIT
        else:
            self.state = MISS

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

class Ship:
    def __init__(self, size):
        self.size = size
        self.orientation = 'horizontal'

class Board:
    def __init__(self, rows, cols):
        self.row_count = rows
        self.col_count = cols
        self.rows = self.build_rows(rows, cols)
        self.header = Header(cols)
        self.ships = []

    def build_rows(self, row_count, col_count):
        rows = []
        for r in range(row_count):
            row = Row()
            for c in range(col_count):
                row.append(EMPTY)
            rows.append(row)
        return rows

    def set_cell(self, col, row, state):
        self.rows[row].set_cell(col, state)

    def print(self):
        self.header.print()
        for index, row in enumerate(self.rows):
            print(f'{index} |', end='')
            row.print()

    def get_position_for_new_ship(self, ship):
        # Find a location for it.
        # This will get more fun as the board becomes more full.
        # TODO vary the size adjustment based on ship.orientation
        x = random.randint(0, self.col_count - 1 - ship.size)
        y = random.randint(0, self.row_count - 1)
        return [x, y]

    def add_ship(self, ship):
        # It seems like the position is a state for the board, not the ship.
        # I'm putting it on the ship for now for convenience.
        ship.position = self.get_position_for_new_ship(ship)
        # Based on the ship's position, we need to alter the cells in the board.
        row = self.rows[ship.position[1]]
        start_col = ship.position[0]
        for i in range(start_col, start_col + ship.size):
            row.set_cell(i, SHIP)

        self.ships.append(ship)

    def fire_at(self, x, y):
        row = self.rows[y]
        cell = row.cells[x]
        cell.shoot()
        # TODO check to see if the boat is gone

rows = 10
cols = 10
board = Board(rows, cols)
ship = Ship(4)
board.add_ship(ship)

board.print()

while True:
    x = int(input('x: '))
    y = int(input('y: '))
    board.fire_at(x, y)
    print('\n'*50)
    board.print()
