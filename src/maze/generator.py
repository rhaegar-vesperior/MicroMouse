"""
Main maze generator interface.
"""

from .constants import MazeConfig
from .grid import MazeGrid
from .algorithms import RecursiveBacktracker
from .loops import LoopInjector


class MazeGenerator:

    def __init__(self, config: MazeConfig | None = None):

        self.config = config or MazeConfig()

    def generate(self):

        grid = MazeGrid(self.config)

        RecursiveBacktracker(
            grid,
            seed=self.config.RANDOM_SEED,
        ).generate()

        LoopInjector(
            grid,
            percentage=self.config.LOOP_PERCENTAGE,
            seed=self.config.RANDOM_SEED,
        ).inject()

        grid.reset_visits()

        return grid