from sympy import *
import numpy as np



def Newton_system(F, J, x, eps):
    """
    Solve nonlinear system F=0 by Newton's method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.
    """
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(F_norm) > eps:
        iteration_counter = -1
    return x, iteration_counter

def test_Newton_system1():
    from numpy import cos, sin, pi, exp

    def F(x):
        x_0 = float(x[0])
        x_1 = float(x[1])

        return np.array(
            [x_0**2 - x_1 + x_0*cos(pi*x_0),
             x_0*x_1 + exp(-x_1) - x_0**(-1)])

    def J(x):
        x_0 = float(x[0])
        x_1 = float(x[1])

        return np.array(
            [[2*x_0 + cos(pi*x_0) - pi*x_0*sin(pi*x_0), -1],
             [x_1 + x_0**(-2), x_0 - exp(-x_1)]])

    expected = np.array([1, 0])
    tol = 1e-4
    x, n = Newton_system(F, J, x=np.array([2, -1]), eps=0.0001)
    print (n, x)


test_Newton_system1()