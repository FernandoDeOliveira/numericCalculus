from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n_row = len(self.matrix)
        self.n_col = len(self.matrix[0])

    @property
    def transpose(self):
        clone_A = [[0 for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                clone_A[j][i] = self.matrix[i][j]
        return clone_A

    def gauss(self):
        n = self.n_row
        A = deepcopy(self.matrix)

        for i in range(0, n):
            # Busca o máximo valor na coluna
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k

            # Troca a linha de valor maior com a linha atual, culuna por coluna
            for k in range(i, n + 1):
                A[maxRow][k], A[i][k] = A[i][k], A[maxRow][k]

            # Faz todas as linhas abaixo zerarem, na coluna em que está
            for k in range(i + 1, n):
                c = -A[k][i] / A[i][i] if A[i][i] != 0 else 0
                for j in range(i, n + 1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]

        # Realiza a retrosubistituição
        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = A[i][n] / A[i][i] if A[i][i] != 0 else 0
            for k in range(i - 1, -1, -1):
                A[k][n] -= A[k][i] * x[i]
        return x

    def rref(self):
        M = deepcopy(self.matrix)
        if not M:
            return
        lead = 0
        for r in range(self.n_row):
            if lead >= self.n_col:
                return M
            i = r
            while M[i][lead] == 0:
                i += 1
                if i == self.n_row:
                    i = r
                    lead += 1
                    if self.n_col == lead:
                        return M
            M[i], M[r] = M[r], M[i]
            lv = M[r][lead]
            M[r] = [mrx / float(lv) for mrx in M[r]]
            for i in range(self.n_row):
                if i != r:
                    lv = M[i][lead]
                    M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
            lead += 1
        return M

    def cholesky(self):
        if self.matrix == self.transpose:
            A = deepcopy(self.matrix)
            n = self.n_row
            L = [[0] * n for _ in range(n)]
            for i, (Ai, Li) in enumerate(zip(A, L)):
                for j, Lj in enumerate(L[:i + 1]):
                    s = sum(Li[k] * Lj[k] for k in range(j))
                    Li[j] = (Ai[i] - s) if (i == j) else (1 / Lj[j] * (Ai[j] - s))
            return L

        else:
            return "matrix isn't symetric"


    def concatena(self, other):
        adjunta = []
        for el1, el2 in zip(self.matrix, other.matrix):
            adjunta.append(el1 + el2)
        return adjunta



if __name__ == "__main__":


    def matrixMul(A, B):
        TB = [i for i in zip(*B)]
        return [[sum(ea * eb for ea, eb in zip(a, b)) for b in TB] for a in A]


    def pivotize(m):
        """Creates the pivoting matrix for m."""
        n = len(m)
        ID = [[float(i == j) for i in range(n)] for j in range(n)]
        for j in range(n):
            row = max(range(j, n), key=lambda i: abs(m[i][j]))
            if j != row:
                ID[j], ID[row] = ID[row], ID[j]
        return ID


    def lu(A):
        """Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
        n = len(A)
        L = [[0.0] * n for i in range(n)]
        U = [[0.0] * n for i in range(n)]
        P = pivotize(A)
        A2 = matrixMul(P, A)
        for j in range(n):
            L[j][j] = 1.0
            for i in range(j + 1):
                s1 = sum(U[k][j] * L[i][k] for k in range(i))
                U[i][j] = A2[i][j] - s1
            for i in range(j, n):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A2[i][j] - s2) / U[j][j]
        return (L, U, P)


    m = Matrix([[1,2],
                [4,5],
                [7,8]])
    adicio = Matrix([[3],[6],[9]])

    concate = m.concatena(adicio)
    print(concate)


    """
    mat = [[3, 1, 9, 15],
           [1, 2, 8, 7],
           [8, 4, 6, 11]]

    m = Matrix(mat)

    l, u, p = lu(mat)

    print(l)
    print(u)


    print(m.gauss())
    """