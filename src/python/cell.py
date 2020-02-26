class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.deg = None
        self.group = None
        self.assigned = False

    def __repr__(self):
        return f"<Cell: ({self.row},{self.col}) ({self.group}, {self.deg})>"

    def neighbours(self, board):
        """ Return the neighbouring cells. 
        """
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

    def update_neighbours(self, board):
        """ Update degrees of neighbouring cells
        Args:
            board (Board): parent board of the cell
        """
        for neighbour in self.neighbours(board):
            neighbour.degree -= 1