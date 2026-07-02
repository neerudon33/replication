import numpy as np

from .constants import PI
from .constants import GF
from .coupling import alpha_s

A0 = 8 * np.pi / 3


def abar_squared(T_ratio):
    """
    Computes ā² from Equation (5).

    Parameters
    ----------
    T_ratio : float
        T/Tc

    Returns
    -------
    float
        ā²
    """

    alpha = alpha_s(T_ratio)

    abar2 = (GF / (2 * PI**2)) * A0 * alpha

    return abar2


from scipy.integrate import quad
import numpy as np


def integrand(x, fg2, abar2):
    """
    Integrand of Equation (5)
    """

    exponent = np.sqrt(x**2 + abar2 * fg2)

    denominator = np.expm1(exponent)

    return x**2 / denominator

def density_integral(fg2, abar2):
    """
    Computes the integral in Equation (5)
    """

    result, error = quad(
        integrand,
        0,
        np.inf,
        args=(fg2, abar2)
    )

    return result