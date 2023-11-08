# Laboratory Work 1: Maze Solver

This is the repository for the first laboratory work of the Computer Graphics course at SPBU University. In this laboratory work, you will implement a maze solver that can respond to queries to determine if it is possible to exit the maze from a given point within a specified time.

## Task Description

**Task**: There is a maze of size (n x n, n <= 10^6) with one exit. You need to implement a program that can respond to queries, given a point and determine whether it is possible to exit the maze from that point within a normal time frame.

**Deadline**: November 18, 2023

## Getting Started

To get started with this laboratory work, follow these steps:

1. Clone this repository to your local machine:

2. Implement the maze solver in your preferred programming language.

3. Test your solution with sample mazes and query scenarios.

4. Document your code and approach in the README file.

5. Make sure to submit your solution by the specified deadline.

## Maze Solver Implementation

You should create a program or script that takes a maze as input and provides a function or method to respond to queries regarding exit possibilities. Please document your code and provide clear instructions on how to use your maze solver.

## Sample Maze Format

Mazes can be represented as 2D grids, where:
- 'S' represents the start point.
- 'E' represents the exit point.
- '#' represents a wall (blocked path).
- '.' represents an open path.

Example:

##########

#S..#####

#.#.#####

#.#...###

#.#.###.#

#.#.#...#

#.###.#.#

#...###.#

#####..E#

##########

## Query Format

Queries will consist of a point's coordinates (x, y). Your program should respond with whether it is possible to exit the maze from that point.
