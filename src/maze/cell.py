"""
Maze cell representation.

Each cell stores the existence of its four walls and
whether it has already been visited during generation.
"""

from dataclasses import dataclass


@dataclass
class Cell:
    """
    Represents one maze cell.
    """

    row: int
    col: int

    north: bool = True
    south: bool = True
    east: bool = True
    west: bool = True

    visited: bool = False

    def wall_count(self) -> int:
        """
        Returns the number of existing walls.
        """

        return sum(
            [
                self.north,
                self.south,
                self.east,
                self.west,
            ]
        )

    def reset(self) -> None:
        """
        Reset visited state.
        """

        self.visited = False