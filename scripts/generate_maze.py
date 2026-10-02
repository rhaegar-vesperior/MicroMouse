from src.maze.generator import MazeGenerator
from src.maze.validator import MazeValidator


def main():

    maze = MazeGenerator().generate()

    validator = MazeValidator(maze)

    print()

    print("Maze generated.")

    print("")

    print("Valid :", validator.validate())

    print("")

    print(f"Rows : {maze.rows}")

    print(f"Cols : {maze.cols}")


if __name__ == "__main__":

    main()