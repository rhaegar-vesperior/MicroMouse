"""
Maze validation utilities.
"""

from collections import deque

from .grid import MazeGrid


class MazeValidator:

    def __init__(self, grid: MazeGrid):

        self.grid = grid

    # --------------------------------------------------------

    def validate(self) -> bool:

        return (
            self._walls_are_consistent()
            and
            self._all_cells_reachable()
        )

    # --------------------------------------------------------

    def _walls_are_consistent(self):

        rows = self.grid.rows
        cols = self.grid.cols

        for r in range(rows):

            for c in range(cols):

                cell = self.grid.cell(r, c)

                # East / West

                if c < cols - 1:

                    right = self.grid.cell(r, c + 1)

                    if cell.east != right.west:

                        return False

                # South / North

                if r < rows - 1:

                    down = self.grid.cell(r + 1, c)

                    if cell.south != down.north:

                        return False

        return True

    # --------------------------------------------------------

    def _all_cells_reachable(self):

        rows = self.grid.rows
        cols = self.grid.cols

        visited = set()

        q = deque()

        q.append((0, 0))

        while q:

            r, c = q.popleft()

            if (r, c) in visited:

                continue

            visited.add((r, c))

            cell = self.grid.cell(r, c)

            if not cell.north and r > 0:
                q.append((r - 1, c))

            if not cell.south and r < rows - 1:
                q.append((r + 1, c))

            if not cell.west and c > 0:
                q.append((r, c - 1))

            if not cell.east and c < cols - 1:
                q.append((r, c + 1))

        return len(visited) == rows * cols