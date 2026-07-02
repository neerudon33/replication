import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, cumulative_trapezoid
from scipy.optimize import root_scalar
from scipy.special import zeta


# Constants & Fixed Model Parameters (Pure Gluon Plasma)

gf = 16          # Gluon degeneracy degrees of freedom (8 colors x 2 polarizations)
nf = 0           # Zero active quark flavors (Pure Gauge theory)
t0 = 0.83        # Calibrated QCD scale parameter \Lambda_T / T_c 

# Ideal gas pQCD limit adjustment constant 
a0 = (np.pi**3) / (12 * zeta(3)) 

# Digitized LGT data points from Boyd et al. (for Figure 1 comparison)
lgt_T = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
lgt_energy = np.array([0.95, 3.62, 4.04, 4.26, 4.42, 4.50, 4.61, 4.66, 4.69, 4.69, 4.71])
lgt_pressure = np.array([0.02, 0.43, 0.76, 0.96, 1.10, 1.21, 1.37, 1.44, 1.49, 1.51, 1.53])


# Equations

def alpha_s(T):
    """2-loop order running coupling constant - Eq. (9)"""
    x = T / t0
    L = np.log(x)
    beta = 3 * (153 - 19 * nf) / (33 - 2 * nf)**2
    return (6 * np.pi / ((33 - 2 * nf) * L)) * (1 - beta * np.log(2 * L) / L)

def abar2(T):
    """Lumped effective interaction strength factor"""
    return (gf / (2 * np.pi**2)) * a0 * alpha_s(T)

def integrand_density(x, fg2, abar):
    """Bose-Einstein momentum integrand for quasiparticle density"""
    exponent = np.sqrt(x*x + abar * fg2)
    if exponent > 700: 
        return 0.0
    return x*x / np.expm1(exponent)

def solve_fg2(T):
    """Solves self-consistent density Eq. (5) via root-finding"""
    abar = abar2(T)
    def residual(fg2):
        val, _ = quad(integrand_density, 0, np.inf, args=(fg2, abar), epsabs=1e-10, epsrel=1e-10)
        return fg2 - val
    
    sol = root_scalar(residual, bracket=[1e-5, 2.5], method="brentq")
    return sol.root

def energy_density_eq6(T, fg2):
    """Calculates epsilon/T^4 using the exact numerical integral from Equation (6)"""
    abar = abar2(T)
    
    # Define the integrand of Equation (6)
    def energy_integrand(x):
        radial_term = np.sqrt(x**2 + abar * fg2)
        exponent = radial_term
        if exponent > 700: # Prevent overflow in expm1
            return 0.0
        return (x**2 * radial_term) / np.expm1(exponent)
    
    # integrate from 0 to infinity
    integral_val, _ = quad(energy_integrand, 0, np.inf, epsabs=1e-10, epsrel=1e-10)
    
    return (gf / (2 * np.pi**2)) * integral_val



# Data Processing Scan

# Scan starts precisely at T/Tc = 0.88 up to 5.0 to handle integration boundaries safely
temperatures = np.linspace(0.88, 5.0, 550)
energy_density_scaled = []

for T in temperatures:
    f_root = solve_fg2(T)
    eps_scaled = energy_density_eq6(T, f_root)
    energy_density_scaled.append(eps_scaled)

energy_density_scaled = np.array(energy_density_scaled)

# Reconstructing standard energy density: epsilon(T) = (epsilon/T^4) * T^4
epsilon_raw = energy_density_scaled * (temperatures**4)

# Thermodynamic Integration to recover Pressure profile (Eq. 8)
# Integrand target: epsilon(T) / T^2
pressure_integrand = epsilon_raw / (temperatures**2)
integrated_value = cumulative_trapezoid(pressure_integrand, temperatures, initial=0.0)

# Set the boundary integration constant to match LGT benchmark at T = T_c (P/T_c^4 = 0.02)
P_inverse_Tc = .002  # LGT benchmark value at T/Tc = 1.0
pressure_scaled = (P_inverse_Tc + integrated_value) / (temperatures**3)


# Plotting Figure 1 Reconstruction

plt.figure(figsize=(8, 6))

# Plot Theoretical Model Curves
plt.plot(temperatures, energy_density_scaled, "--", color="black", label=r"Model $\epsilon/T^4$")
plt.plot(temperatures, pressure_scaled, ":", color="black", label=r"Model $P/T^4$")

# Plot Discrete LGT Experimental Symbols
plt.scatter(lgt_T, lgt_energy, marker="x", color="black", s=40, label=r"Lattice $\epsilon/T^4$")
plt.scatter(lgt_T, lgt_pressure, marker="+", color="black", s=50, label=r"Lattice $P/T^4$")

# Layout refinements
plt.text(1.3, 4.3, r"$\epsilon/T^4$", fontsize=13)
plt.text(1.5, 0.5, r"$P/T^4$", fontsize=13)

plt.xlim(0.5, 5.0)
plt.ylim(0.0, 5.0)
plt.xlabel(r"$T/T_c$", fontsize=12)
plt.ylabel(r"$\epsilon/T^4, \quad P/T^4$", fontsize=12)
plt.legend(loc="lower right")
plt.grid(True, linestyle=":", alpha=0.5)

plt.tight_layout()
plt.show()

print("final energy density values:", energy_density_scaled[-1])
print("final pressure values:", pressure_scaled[-1])