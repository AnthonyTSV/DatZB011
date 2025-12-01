from SEIR0 import SEIR0, solve_SEIR
from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

class SEIR(SEIR0):
    def __init__(
        self, beta, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2
    ):
        ...

    def __call__(self, t, u):
        ...


def test_SEIR_beta_const():
    raise NotImplementedError(
        "Implement test_SEIR_beta_const function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


def test_SEIR_beta_var():
    raise NotImplementedError(
        "Implement test_SEIR_beta_var function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


def plot_SEIR(t, u, components=["S", "I", "Ia", "R"]):
    raise NotImplementedError(
        "Implement plot_SEIR function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


if __name__ == "__main__":
    test_SEIR_beta_const()
    test_SEIR_beta_var()
    model = SEIR(beta = 0.4)
    t, u = solve_SEIR(model, T = 200, N = 400,
    S_0 = 5.5e6, E2_0 = 100)
    plot_SEIR(t,u)
