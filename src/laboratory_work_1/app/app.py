import re

import numpy as np

from src.laboratory_work_1.src.maze_solver import MazeSolver


def get_maze():
    n = int(input("Maze size: "))

    maze = []
    symbols = {".", "#", "S", "E"}

    for i in range(n):
        line = input(f"> ")

        while len(line) != n or not set(line).issubset(symbols):
            line = input(f"> ")

        maze += [list(line)]

    return maze


def app():
    print(
        "Just simple app that can find out is it possible to reach the exit of the maze 🍰"
    )
    maze = get_maze()
    start_point = tuple(*np.argwhere(np.array(maze) == "S"))
    exit_point = tuple(*np.argwhere(np.array(maze) == "E"))
    solver = MazeSolver(
        [list(map(lambda x: re.sub("S|E", ".", x), line)) for line in maze]
    )

    print(
        "Yes, it is possible to reach the exit"
        if solver.exec_query(start_point, exit_point)
        else "NO, it is not possible to reach the exit"
    )


if __name__ == "__main__":
    app()
