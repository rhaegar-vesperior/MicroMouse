"""
Maze generation algorithms.

Currently implements Recursive Backtracker (Depth First Search).

Produces a perfect maze where every cell is reachable and
there is exactly one path between any two cells.
"""

from __future__ import annotations

import random

from .grid import MazeGrid
from .cell import Cell


class RecursiveBacktracker:
    """
    Recursive Backtracker maze generator.
    """

    def __init__(self, grid: MazeGrid, seed: int | None = None):

        self.grid = grid

        self.random = random.Random(seed)

    # --------------------------------------------------------
    # Public API
    # --------------------------------------------------------

    def generate(self) -> MazeGrid:

        start = self.grid.cell(0, 0)

        self._visit(start)

        return self.grid

    # --------------------------------------------------------
    # Internal DFS
    # --------------------------------------------------------

    def _visit(self, current: Cell):

        current.visited = True

        neighbours = self._unvisited_neighbours(current)

        while neighbours:

            direction, neighbour = self.random.choice(neighbours)

            if not neighbour.visited:

                self._remove_wall(current, neighbour, direction)

                self._visit(neighbour)

            neighbours = self._unvisited_neighbours(current)

    # --------------------------------------------------------
    # Find neighbours
    # --------------------------------------------------------

    def _unvisited_neighbours(self, cell: Cell):

        r = cell.row
        c = cell.col

        neighbours = []

        directions = [

            (-1, 0, "north"),

            (1, 0, "south"),

            (0, -1, "west"),

            (0, 1, "east")

        ]

        for dr, dc, direction in directions:

            nr = r + dr
            nc = c + dc

            if self.grid.in_bounds(nr, nc):

                neighbour = self.grid.cell(nr, nc)

                if not neighbour.visited:

                    neighbours.append((direction, neighbour))

        return neighbours

    # --------------------------------------------------------
    # Remove wall between cells
    # --------------------------------------------------------

    @staticmethod
    def _remove_wall(current: Cell,
                     neighbour: Cell,
                     direction: str):

        if direction == "north":

            current.north = False
            neighbour.south = False

        elif direction == "south":

            current.south = False
            neighbour.north = False

        elif direction == "east":

            current.east = False
            neighbour.west = False

        elif direction == "west":

            current.west = False
            neighbour.east = False