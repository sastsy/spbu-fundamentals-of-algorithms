from time import perf_counter
from collections import deque
import os


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def is_valid(i: int, j: int, maze: list, checked_cells: list) -> bool:
    return i > -1 and i < len(maze) and j > -1 and j < len(maze[0]) and maze[i][j] != '#' and not checked_cells[i][j]


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"

    i, j = len(maze.list_view), len(maze.list_view[0])
    checked_cells = [[0] * j for _ in range(i)]

    queue = deque()
    queue.append((path, 0, maze.start_j))

    is_found = False

    while queue:
        path, i, j = queue.popleft()
        checked_cells[i][j] = 1

        for step in ['L', 'R', 'U', 'D']:
            pos_i, pos_j = _shift_coordinate(i, j, step)
            if is_valid(pos_i, pos_j, maze.list_view, checked_cells):
                queue.append((path + step, pos_i, pos_j))
                if maze.list_view[pos_i][pos_j] == 'X':
                    is_found = True
                    break
        
        if is_found:
            break

    print(f"Found: {path}")
    maze.print(path)


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("spbu-fundamentals-of-algorithms/practicum_2/homework/maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
