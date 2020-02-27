import random


class Cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.degree = -1
        self.group = -1
        self.assigned = False

    def __repr__(self):
        return f"<Cell: ({self.row},{self.col}) ({self.group}, {self.degree})>"

    def neighbours(self, board):
        """ Return the neighbouring cells. 
        """
        for r, c in random.sample(list({
            "left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down:": (1, 0)
        }.values()), 4):
            if (
                (0 <= self.row + r < board.nrow) and
                (0 <= self.col + c < board.ncol)
            ):
                yield board.grid[self.row + r][self.col + c]

    def update_neighbours(self, board):
        """ Update degrees of neighbouring cells
        Args:
            board (Board): parent board of the cell
        """
        for neighbour in self.neighbours(board):
            neighbour.degree -= 1