from random import randint

from cell import Cell


class Board:

    def __init__(self, nrow, ncol):
        self._nrow = nrow
        self._ncol = ncol
        self._grid = [
            [Cell(r, c) for c in range(ncol)]
            for r in range(nrow)
        ]
        
        self.assign_degree()

    @property
    def nrow(self):
        return self._nrow

    @property
    def ncol(self):
        return self._ncol

    @property
    def grid(self):
        return self._grid

    def print_board(self):
        for row in self._grid:
            for cell in row:
                print(f"{cell.group:2}", end="|")
            print("")

    def assign_degree(self):
        for row in self._grid:
            for cell in row:
                degree = 4
                if cell.row == 0 or cell.row == self.nrow-1:
                    degree -= 1
                if cell.col == 0 or cell.col == self.ncol-1:
                    degree -= 1
                cell.degree = degree

    def divide_board(self, ngroup):
        nrow = self.nrow
        ncol = self.ncol

        if nrow*ncol % ngroup != 0:
            raise Exception(f"Board can't be divided into {ngroup} equal groups")

        cells_per_group = nrow*ncol // ngroup
        init_row = randint(0, nrow-1)
        init_col = randint(0, ncol-1)
        init_cell = self._grid[init_row][init_col]

        self.recurse_cells(init_cell, cells_per_group, 1)

    def recurse_cells(self, cell, cells_per_group, assigned_count):
        if cell:
            cell.group = (self.nrow*self.ncol - assigned_count) // cells_per_group
            cell.assigned = True
            self.recurse_cells(
                self.next_cell(cell), cells_per_group, assigned_count + 1)

    def next_cell(self, cell):
        min_degree = 4
        next_cell = None

        for neighbour in cell.neighbours(self):
            if not neighbour.assigned:
                deg = neighbour.degree
                deg -= 1
                if min_degree > deg:
                    next_cell = neighbour
                    min_degree = deg
        return next_cell


if __name__ == "__main__":
    board = Board(4, 40)
    board.divide_board(16)
    board.print_board()
