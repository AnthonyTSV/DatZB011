from SEIR import SEIR

class SEIRimport(SEIR):
    ...

if __name__ == "__main__":
    from SEIR import SEIR, solve_SEIR, plot_SEIR
    from lockdown import Beta
    beta = Beta("beta_values.txt")
    beta.plot(1000)

    model = SEIRimport(beta, sigma=10)
    t, u = solve_SEIR(model, T=1000, N=1000,
                      S_0=5.5e6, E2_0=100)
    plot_SEIR(t, u, components=["I", "Ia"])