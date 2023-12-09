from typing import Union, Any

import numpy as np


class DisjointSetUnion:
    def __init__(self, n: int) -> None:
        self.parent = np.arange(n**2, dtype=int)
        self.rank = np.zeros(n**2, dtype=int)

    def find(self, v: Union[Any, np.dtype]) -> Union[Any, np.dtype]:
        self.parent[v] = (
            self.find(self.parent[v]) if v != self.parent[v] else self.parent[v]
        )
        return self.parent[v]

    def union(self, u: Union[Any, np.dtype], v: Union[Any, np.dtype]) -> None:
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                root1, root2 = root2, root1
            self.parent[root1] = root2
            if self.rank[root1] == self.rank[root2]:
                self.rank[root2] += 1
