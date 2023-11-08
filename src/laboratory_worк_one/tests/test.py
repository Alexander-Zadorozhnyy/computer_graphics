from src.laboratory_worк_one.src.maze_solver import MazeSolver
from src.laboratory_worк_one.tests.test_cases import mazes


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
# def test_maze_solver_big():
#     n = 1920
#
#     temp1 = ["."]
#     temp2 = ["#"] * (n - 1)
#     temp1.extend(temp2)
#     labyrinth = [temp1] * n
#
#     maze_solver = Maze_Solver(labyrinth, n)
#
#     for i in range(1, 1920):
#        assert maze_solver.query(0, 0, (n - i, 0), n) == True
