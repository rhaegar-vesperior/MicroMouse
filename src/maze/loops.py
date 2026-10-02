"""
Loop injection for perfect mazes.

Removes a configurable number of internal walls to create
multiple valid paths while preserving connectivity.
"""

from __future__ import annotations

import random

from .grid import MazeGrid


class LoopInjector:

    def __init__(
        self,
        grid: MazeGrid,
        percentage: float = 0.10,
        seed: int | None = None,
    ):

        self.grid = grid
        self.percentage = percentage
        self.random = random.Random(seed)

    def inject(self) -> MazeGrid:

        candidates = []

        rows = self.grid.rows
        cols = self.grid.cols

        # Only consider east and south walls to avoid duplicates
        for r in range(rows):

            for c in range(cols):

                cell = self.grid.cell(r, c)

                if c < cols - 1 and cell.east:
                    candidates.append(("east", r, c))

                if r < rows - 1 and cell.south:
                    candidates.append(("south", r, c))

        self.random.shuffle(candidates)

        remove_count = int(len(candidates) * self.percentage)

        removed = 0

        for direction, r, c in candidates:

            if removed >= remove_count:
                break

            current = self.grid.cell(r, c)

            if direction == "east":

                neighbour = self.grid.cell(r, c + 1)

                current.east = False
                neighbour.west = False

            else:

                neighbour = self.grid.cell(r + 1, c)

                current.south = False
                neighbour.north = False

            removed += 1

        return self.grid