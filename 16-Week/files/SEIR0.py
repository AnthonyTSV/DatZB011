import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4, ODESolver


class SEIR0:
    def __init__(
        self, beta=0.33, r_ia=0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2
    ):

        self.beta = beta
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

    def __call__(self, t, u):
        beta = self.beta
        r_ia = self.r_ia
        r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1
        lmbda_2 = self.lmbda_2
        p_a = self.p_a
        mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta * S * I / N - r_ia * beta * S * Ia / N - r_e2 * beta * S * E2 / N
        dE1 = (
            beta * S * I / N
            + r_ia * beta * S * Ia / N
            + r_e2 * beta * S * E2 / N
            - lmbda_1 * E1
        )
        dE2 = lmbda_1 * (1 - p_a) * E1 - lmbda_2 * E2
        dI = lmbda_2 * E2 - mu * I
        dIa = lmbda_1 * p_a * E1 - mu * Ia
        dR = mu * (I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


def test_SEIR0():

    expected_du = [-0.12925, -0.20075, -0.302, 0.3, -0.068, 0.4]

    raise NotImplementedError(
        "Implement test_SEIR0 function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


def solve_SEIR(model: SEIR0, T, N, S_0, E2_0):

    raise NotImplementedError(
        "Implement solve_SEIR function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


def plot_SEIR(t, u):
    raise NotImplementedError(
        "Implement plot_SEIR function."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING


if __name__ == "__main__":
    model = SEIR0(beta = 0.4)
    raise NotImplementedError(
        "Implement main block to test the SEIR0 model."
    )  # REMOVE THIS LINE WHEN IMPLEMENTING
