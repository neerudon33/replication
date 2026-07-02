#computing alpha_s for different values of T/Tc
import numpy as np
from src.coupling import alpha_s

temps = [1.0, 1.5, 2.0, 3.0, 5.0]

print(" T/Tc      alpha_s")

for T in temps:
    print(f"{T:5.2f}     {alpha_s(T):.6f}")

#finding ā² for T/Tc = 2.0
from src.integrals import abar_squared

print("ā² =", abar_squared(2.0))

#finding the integral in Equation (5) for fg² = 1.0 and T/Tc = 2.0
from src.integrals import density_integral

abar2 = abar_squared(2.0)

I = density_integral(1.0, abar2)

print("Integral =", I)

#finding fg² for T/Tc = 2.0
from src.solver import solve_fg2

from src.temperature_scan import scan_temperature
from src.plotting import plot_fg2
from src.io_utils import save_fg2
from src.plotting import plot_figure2

temperature, fg2_values, omega = scan_temperature()

plot_figure2(
    temperature,
    fg2_values,
    omega
)

fg2 = solve_fg2(2.0)
print("fg² =", fg2)
###
print("\nFirst five values")

for T, fg in zip(temperature[:5], fg2_values[:5]):
    print(f"T/Tc = {T:.2f}   fg² = {fg:.6f}")

print("\nLast five values")

for T, fg in zip(temperature[-5:], fg2_values[-5:]):
    print(f"T/Tc = {T:.2f}   fg² = {fg:.6f}")

from src.solver import residual

fg2 = solve_fg2(2.0)

print("Residual =", residual(fg2, 2.0))

for T in [1.5, 2.0, 5.0]:
    print(T, solve_fg2(T))