from itertools import product
from typing import List, Tuple

from src.laboratory_worк_1.src.disjoint_set_union import DisjointSetUnion


class MazeSolver:
    def __init__(self, maze: List[List[str]]) -> None:
        self.dim = len(maze)
        self.dsu = DisjointSetUnion(self.dim)

        self.__fill_dsu(maze)

    def __index(self, i: int, j: int) -> int:
        return self.dim * i + j

    def __fill_dsu(self, maze: List[List[str]]) -> None:
        for x, y in product(range(self.dim), repeat=2):
            if x + 1 < self.dim and maze[x][y] == "." and maze[x + 1][y] == ".":
                self.dsu.union(self.__index(x, y), self.__index(x + 1, y))

            if y + 1 < self.dim and maze[x][y] == "." and maze[x][y + 1]:
                self.dsu.union(self.__index(x, y), self.__index(x, y + 1))

    def exec_query(
        self, start_point: Tuple[int, int], exit_point: Tuple[int, int]
    ) -> bool:
        return self.dsu.find(self.__index(*start_point)) == self.dsu.find(
            self.__index(*exit_point)
        )
