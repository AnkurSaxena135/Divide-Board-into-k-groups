class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.group = -1
        self.assigned = False

    def __repr__(self):
        return f"<Cell: ({self.row},{self.col}) ({self.group})>"

    def __gt__(self, other):
        return self.deg > other.deg

    def is_assigned(self):
        return self.assigned

    def neighbours(self, board):
        for r, c in {
            "left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down:": (1, 0)
        }.values():
            if (
                (0 <= self.row + r < board.nrow) and
                (0 <= self.col + c < board.ncol)
            ):
                yield board.grid[self.row + r][self.col + c]
