from src.laboratory_worк_1.src.maze_solver import MazeSolver
from src.laboratory_worк_1.tests.test_cases import mazes


def test_maze_solver():
    for case in mazes:
        maze_solver = MazeSolver(case["maze"])

        for test in case["tests"]:
            assert (
                maze_solver.exec_query(test["start_point"], test["exit_point"])
                == test["result"]
            )


if __name__ == "__main__":
    test_maze_solver()
