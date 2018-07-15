f_x = [1.00, 1.41, 1.73, 2.00, 2.24, 2.45, 2.65, 2.83, 3.00, 3.16]
X = [1.04, 1.37, 1.70, 2.00, 2.26, 2.42, 2.70, 2.78, 3.00, 3.14]
_x_ = 1.55


def neville(x, y, _x_):
    n = len(y)
    Q = [[0 for i in range(n)] for j in range(n)]
    for i, el in enumerate(y):
        Q[i][0] = el

    for i in range(n):
        for j in range(i):
            j += 1
            Q[i][j] = ((_x_ - x[i - j]) * Q[i][j - 1] - (_x_ - x[i]) * Q[i - 1][j - 1]) / (x[i] - x[i - j])
    return Q, Q[-1][-1]


Qs, Qnn = neville(X, f_x, _x_)
print(Qnn)
