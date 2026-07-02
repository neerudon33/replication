import numpy as np

from .solver import solve_fg2

def scan_temperature():

    temperatures = np.linspace(1.0, 5.0, 50)

    fg2_values = []

    for T in temperatures:

        print(f"Solving T/Tc = {T:.2f}")

        fg2 = solve_fg2(T)

        fg2_values.append(fg2)

    fg2_values = np.array(fg2_values)
    omega = (2 / (3 * np.pi)) * fg2_values
    return temperatures, fg2_values, omega
temperature, fg2_values, omega = scan_temperature()
print("\nLast five values")

for T, fg in zip(temperature[-5:], fg2_values[-5:]):
    print(f"T/Tc = {T:.2f}   fg² = {fg:.6f}")

