import os
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


class Beta:
    """Piecewise constant beta parameter loaded from file."""

    def __init__(self, filename):
        self.reference_date = date(2020, 2, 15)
        self.filepath = os.path.join(os.path.dirname(__file__), filename)
        self._load_beta_schedule()

    def _load_beta_schedule(self):
        raise NotImplementedError(
            "Implement _load_beta_schedule method to read beta values from file."
        )  # REMOVE THIS LINE WHEN IMPLEMENTING

    def __call__(self, t):
        raise NotImplementedError(
            "Implement __call__ method to return beta value for time t."
        )  # REMOVE THIS LINE WHEN IMPLEMENTING

    def plot(self, T):
        raise NotImplementedError(
            "Implement plot method to visualize beta over time."
        )  # REMOVE THIS LINE WHEN IMPLEMENTING

    def str2date(self, date_str):
        """
        Convert a date string on the format dd.mm.yyyy
        to a datetime.date object
        """
        day, month, year = (int(n) for n in date_str.split("."))
        return date(year, month, day)


if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR

    beta = Beta("beta_values.txt")
    beta.plot(1000)

    model = SEIR(beta)
    t, u = solve_SEIR(model, T=1000, N=1000, S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components=["I", "Ia"])
