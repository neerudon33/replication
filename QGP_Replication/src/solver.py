from scipy.optimize import root_scalar

from .integrals import density_integral
from .integrals import abar_squared
def residual(fg2, T_ratio):
    """
    Residual of Equation (5).

    Returns

        fg² - Integral
    """

    abar2 = abar_squared(T_ratio)

    integral = density_integral(fg2, abar2)

    return fg2 - integral
def solve_fg2(T_ratio):

    solution = root_scalar(
        residual,
        args=(T_ratio,),
        bracket=[0.01,10],
        method="brentq"
    )

    return solution.root
