import numpy as np

# Model parameters
nf = 0          # Number of quark flavours
t0 = 0.83       # Lambda_T / Tc


def alpha_s(T_ratio):
    T_ratio = np.asarray(T_ratio, dtype=float)

    x = T_ratio / t0

    if np.any(x <= 1):
        raise ValueError(
            "T/Lambda_T must be > 1 because the logarithm becomes undefined."
        )

    L = np.log(x)

    beta = (
        3 * (153 - 19 * nf)
        / (33 - 2 * nf) ** 2
    )

    alpha = (
        6 * np.pi
        / ((33 - 2 * nf) * L)
    ) * (
        1
        - beta * np.log(2 * L) / L
    )

    return alpha