"""
Maze grid.

Responsible only for creating and storing cells.
No maze-generation logic belongs here.
"""

from .cell import Cell
from .constants import MazeConfig


class MazeGrid:
    """
    Stores all maze cells.
    """

    def __init__(self, config: MazeConfig):

        self.config = config

        self.rows = config.ROWS
        self.cols = config.COLS

        self.grid = [
            [
                Cell(r, c)
                for c in range(self.cols)
            ]
            for r in range(self.rows)
        ]

    def cell(self, row: int, col: int) -> Cell:
        return self.grid[row][col]

    def in_bounds(self, row: int, col: int) -> bool:
        return (
            0 <= row < self.rows
            and
            0 <= col < self.cols
        )

    def reset_visits(self) -> None:

        for row in self.grid:
            for cell in row:
                cell.visited = False