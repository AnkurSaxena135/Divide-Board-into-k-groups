from random import randint
from cell import Cell
from board_gui import BoardGUI


class Board:
    def __init__(self, nrow, ncol):
        self.nrow = nrow
        self.ncol = ncol
        self.grid = [
            [Cell(r, c) for c in range(ncol)]
            for r in range(nrow)
        ]
        self.assign_degree()
        self.gui = BoardGUI(self)

    def divide_board(self, ngroup):
        """Divide board into n equal groups
        Args:
            ngroup (int): number of group
        Raises:
            ValueError: if division into 
                n groups is not possible
        """
        if self.nrow*self.ncol % ngroup != 0:
            raise ValueError(
                f"Can't divide board into {ngroup} equal groups")

        init_cell = self.get_random_cell()
        cells_per_group = self.nrow*self.ncol // ngroup
        self.assign_recursively(init_cell, 1, cells_per_group)

    def assign_recursively(self, cell, cell_number, cells_per_group):
        """ Recursively assign a group to each cell
        Args:
            cell (Cell): current cell whwich needs to be assigned
            cell_number (int): the order of current cell 
                Value increases serially. Range: [1, row* col]
                i.e. 1 means 1st cell to be assigned
            cells_per_group (int): cells per group
                constant value passed to avoid recalculation
        """
        cell.group = (self.nrow*self.ncol - cell_number) // cells_per_group
        cell.assigned = True
        cell.update_neighbours(self)
        next_cell = self.next_cell(cell)
        if next_cell:
            self.assign_recursively(
                next_cell,
                cell_number + 1,
                cells_per_group
            )

    def next_cell(self, cell):
        """ Get the next cell by selecting the neighbouring cell
        with lowest degree
        Args:
            cell (Cell): current cell
        Returns:
            cell (Cell): next neighbouring cell with lowest degree
        """
        min_degree = 4
        next_cell = None

        for neighbour in cell.neighbours(self):
            if not neighbour.assigned:
                deg = neighbour.degree
                if min_degree > deg:
                    next_cell = neighbour
                    min_degree = deg
        return next_cell

    def assign_degree(self):
        """ Assign degree to all cells on the board. Degree of a
        cell means the number of unassigned cells in it's neighbourhood.
        Example:
            degress on a 3x3 board
            |2|3|2|
            |3|4|3|
            |2|3|2|
        """
        for row in self.grid:
            for cell in row:
                degree = 4
                if cell.row == 0 or cell.row == self.nrow-1:
                    degree -= 1
                if cell.col == 0 or cell.col == self.ncol-1:
                    degree -= 1
                cell.degree = degree

    def print_board(self):
        """Print the board on console"""
        for row in self.grid:
            for cell in row:
                print(f"{cell.group:2}", end="|")
            print("")

    def display_board(self):
        """Display gui for the board"""
        self.gui.display()

    def get_random_cell(self):
        """Select a random cell from the board"""
        return self.grid[randint(0, self.nrow-1)][randint(0, self.ncol-1)]


if __name__ == "__main__":
    board = Board(4, 5)
    board.divide_board(5)
    board.display_board()
