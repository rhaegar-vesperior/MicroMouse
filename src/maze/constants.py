"""
Maze constants and global configuration.

This file contains only constant values that define the maze geometry.
No generation logic should appear here.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MazeConfig:
    """
    Global maze configuration.

    All units are SI (meters) where applicable.
    """

    # Maze dimensions
    ROWS: int = 16
    COLS: int = 16

    # Physical dimensions
    CELL_SIZE: float = 0.30
    WALL_THICKNESS: float = 0.02
    WALL_HEIGHT: float = 0.08

    # Loop generation
    LOOP_PERCENTAGE: float = 0.10

    # Random seed
    RANDOM_SEED: int | None = None

    # Entrance
    START_ROW: int = 0
    START_COL: int = 0

    # Exit
    EXIT_ROW: int = ROWS - 1
    EXIT_COL: int = COLS - 1