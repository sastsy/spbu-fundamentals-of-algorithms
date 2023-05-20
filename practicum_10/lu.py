import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    for column in range(len(A)):
        if permute:
            P = np.eye(len(A))
            max_pivot = np.NINF
            max_pivot_row = 0
            for row in range(column, len(A[column])):
                if A[row][column] > max_pivot:
                    max_pivot = A[row][column]
                    max_pivot_row = row
            P[column], P[max_pivot_row] = P[max_pivot_row], P[column].copy()
            A = np.dot(P, A)
        U, L = A.copy(), np.eye(len(A))
        for row in range(column + 1, len(A[column])):
            E_inv = np.eye(len(A))
            E_inv[row][column] = U[row][row] / U[column][column]
            U[row] -= U[column] * (U[row][row] / U[column][column])
            L = np.dot(L, E_inv)
    
    return tuple([L, U, P])


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                L[i][j] = -L[i][j]
                U[i][j] = -U[i][j]
    return np.dot(np.dot(np.dot(U, L), P), b)


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 14  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    print(L, U, P, end='\n')
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"