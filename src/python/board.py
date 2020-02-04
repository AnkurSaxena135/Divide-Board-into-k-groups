from random import randint
from queue import PriorityQueue

from cell import Cell


class Board:

    def __init__(self, nrow, ncol):
        self.nrow = nrow
        self.ncol = ncol
        self.grid = [
            [Cell(r, c) for c in range(ncol)]
            for r in range(nrow)
        ]
        self.degree = [
            [self.assign_degree(r, c) for c in range(ncol)]
            for r in range(nrow)
        ]

    def print_board(self):
        for row in self.grid:
            for cell in row:
                print(f"{cell.group:2}", end="|")
            print("")

    def assign_degree(self, row, col):
        degree = 4
        if row == 0 or row == self.nrow-1:
            degree -= 1
        if col == 0 or col == self.ncol-1:
            degree -= 1
        return degree

    def divide_board(self, ngroup):
        nrow = self.nrow
        ncol = self.ncol
        pq = PriorityQueue(nrow*ncol)

        if nrow*ncol % ngroup != 0:
            raise Exception(f"Board can't be divided into {ngroup} equal groups")
        group_size = nrow*ncol // ngroup

        init_cell = self.grid[randint(0, nrow-1)][randint(0, ncol-1)]

        pq.put((self.degree[init_cell.row][init_cell.col], init_cell))
        self.recurse_cells(pq, group_size, 1)

    def recurse_cells(self, pq, group_size, count):
        try:
            deg, cell = pq.get(False)
            while cell.is_assigned():
                deg, cell = pq.get(False)
        except:
            return
        
        cell.group = (self.nrow*self.ncol - count) // group_size
        cell.assigned = True
        if (self.nrow*self.ncol - count) % group_size == 0:
            pq = PriorityQueue()
        self.print_board()
        self.update_neighbours(cell, pq)
        return self.recurse_cells(pq, group_size, count + 1)

    def update_neighbours(self, cell, pq):
        for neighbour in cell.neighbours(self):
            if not neighbour.is_assigned():
                deg = self.degree[neighbour.row][neighbour.col]
                deg -= 1
                neighbour.deg = deg
                pq.put((deg, neighbour))


if __name__ == "__main__":
    board = Board(4, 4)
    board.divide_board(16)
    board.print_board()
