n = 1000

mazes = [
    {
        "maze": [
            ["#", "#", ".", "#"],
            ["#", ".", ".", "#"],
            [".", ".", "#", "#"],
            ["#", ".", "#", "."],
        ],
        "tests": [
            {"start_point": (2, 0), "exit_point": (1, 2), "result": True},
            {"start_point": (3, 1), "exit_point": (0, 2), "result": True},
            {"start_point": (3, 3), "exit_point": (0, 2), "result": False},
        ],
    },
    {
        "maze": [
            ["#", ".", "#", "#", ".", "."],
            ["#", ".", ".", "#", "#", "#"],
            ["#", "#", ".", ".", ".", "."],
            ["#", ".", "#", "#", ".", "."],
            ["#", ".", ".", "#", ".", "."],
            ["#", "#", "#", "#", "#", "#"],
        ],
        "tests": [
            {"start_point": (0, 1), "exit_point": (4, 5), "result": True},
            {"start_point": (4, 1), "exit_point": (0, 1), "result": False},
            {"start_point": (4, 5), "exit_point": (1, 5), "result": False},
            {"start_point": (4, 1), "exit_point": (2, 4), "result": False},
            {"start_point": (2, 3), "exit_point": (2, 5), "result": True},
        ],
    },
    {
        "maze": [["#", "."] * (n // 2)] * n,
        "tests": [
            {"start_point": (0, k), "exit_point": (n - 1, k), "result": True}
            for k in range(1, n, 2)
        ]
        + [
            {"start_point": (k, 0), "exit_point": (k, n - 1), "result": False}
            for k in range(1, n, 2)
        ],
    },
]
