from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def cross_product(p1: NDArray, p2: NDArray, r: NDArray) -> int:
    return  (p1[0] - r[0]) * (p2[1] - r[1]) - (p1[1] - r[1]) * (p2[0] - r[0])


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    index = np.lexsort((points[:, 1], -points[:, 0]))
    sorted_points = points[index]
    lower_vertices = []
    print(sorted_points)
    
    for point in sorted_points:
        while len(lower_vertices) > 1 and cross_product(point, lower_vertices[-1], lower_vertices[-2]) <= 0:
            lower_vertices.pop()
        lower_vertices.append(point)

    return np.array(lower_vertices)


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"spbu-fundamentals-of-algorithms/practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
