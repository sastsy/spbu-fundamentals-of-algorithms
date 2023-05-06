import numpy as np


def lu(A, permute):
    n = len(A)
    U = np.copy(A)
    L = np.eye(n)
    P = np.eye(n)
    for k in range(n - 1):
        P_0 = np.eye(n)
        U_0 = np.eye(n)
        L_0 = np.eye(n)
        if permute:
            max_elem = U[k, k]
            i_max = k
            for i in range(k + 1, n):
                if abs(max_elem) < abs(U[i, k]):
                    max_elem = U[i, k]
                    i_max = i
            P_0[i_max], P_0[k] = P_0[k].copy(), P_0[i_max].copy()
            U = P_0 @ U
        for i in range(k + 1, n):
            c = U[i, k] / U[k, k]
            U_0[i, k] = -c
            L_0[i, k] = c
        U = U_0 @ U
        P = P_0 @ P
        L = L @ (P_0 @ L_0)
    L = P.dot(L)
    return L, U, P


def solve(L, U, P, b):
    n = len(L)
    x = [0] * n
    y = [0] * n
    for i in range(n):
        s = sum(L[i, j] * y[j] for j in range(i))
        y[i] = b[np.where(P[i] == 1)[0][0]] - s
    for i in reversed(range(n)):
        s = sum(U[i, j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s) / U[i, i]
    return x


def get_A_b(a_1_1, b_1):
    A = [[a_1_1, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]]
    b = [b_1, 12.0, -39.0]
    return A, b


if __name__ == "__main__":
    a_1_1 = 3 + 10 ** (-14)  # add 10^{-p} to check instability
    b_1 = -16 + 10 ** (-14)  # add 10^{-p} to check instability
    A, b = get_A_b(a_1_1, b_1)
    L, U, P = lu(A.copy(), True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4]))
    L, U, P = lu(A.copy(), False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4]))
