f_x = [1.00, 1.41, 1.73, 2.00, 2.24, 2.45, 2.65, 2.83, 3.00, 3.16]
X = [1.04, 1.37, 1.70, 2.00, 2.26, 2.42, 2.70, 2.78, 3.00, 3.14]
_x_ = 1.55


def newtonDividedDiff(X, f_x, _x_):
    n = len(f_x)
    F = [[0 for i in range(n)] for j in range(n)]
    for i, el in enumerate(f_x):
        F[i][0] = el

    for i in range(n):
        for j in range(i):
            j += 1
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (X[i] - X[i - j])

    def P(_x_, F, X):
        p_x = 0
        for i in range(len(F)):
            prod = 1
            for j in range(i):
                prod *= (_x_ - X[j])
            p_x += F[i][i] * prod

        return p_x

    return P(_x_=_x_, F=F, X=X)


newts = newtonDividedDiff(X=X, f_x=f_x, _x_=_x_)
print(newts)
