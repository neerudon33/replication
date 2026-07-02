import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import root_scalar
from scipy.special import zeta


# Constants & Fixed Parameters

gf = 16
nf = 0
t0 = 0.83  # \Lambda_T / T_c 

# Correct a_0 derived from the asymptotic QCD limit 
a0 = (np.pi**3) / (12 * zeta(3)) 


# Running Coupling alpha_s(T) - Eq. (9)
    
def alpha_s(T):
    x = T / t0
    L = np.log(x)
    beta = 3 * (153 - 19 * nf) / (33 - 2 * nf)**2
    return (6 * np.pi / ((33 - 2 * nf) * L)) * (1 - beta * np.log(2 * L) / L)


# Effective Coupling parameter \overline{a}²

def abar2(T):
    return (gf / (2 * np.pi**2)) * a0 * alpha_s(T)


# Self-Consistent Density Solver - Eq. (5)

def integrand(x, fg2, abar):
    exponent = np.sqrt(x*x + abar * fg2)
    if exponent > 700:  # Prevent overflow
        return 0.0
    return x*x / np.expm1(exponent)

def integral(fg2, abar):
    value, _ = quad(
        integrand, 0, np.inf, args=(fg2, abar),
        epsabs=1e-10, epsrel=1e-10, limit=500
    )
    return value

def residual(fg2, T):
    return fg2 - integral(fg2, abar2(T))

def solve_fg2(T):
    # Near T_c, fg2 drops close to 0
    sol = root_scalar(
        residual, args=(T,), bracket=[1e-5, 2.5], method="brentq"
    )
    return sol.root


# Data Generation

# Scan starts slightly above the singularity line (~0.83) up to 5.0
temperature = np.linspace(0.84, 5.0, 200)

alpha_vals = []
fg2_vals = []
omega_vals = []

for T in temperature:
    a = alpha_s(T)
    f = solve_fg2(T)
    
    # Corrected conversion to plasma frequency ratio [cite: 54, 75]
    w = (2 * a0 / np.pi**3) * f  
    
    alpha_vals.append(a)
    fg2_vals.append(f)
    omega_vals.append(w)


# Plotting Figure 2 Replication

plt.figure(figsize=(7, 5.5))

# Plot lines style 
plt.plot(temperature, fg2_vals, "--", color="black", label=r"$f_g^2$")
plt.plot(temperature, alpha_vals, ":", color="black", label=r"$\alpha_s$")
plt.plot(temperature, omega_vals, "-", color="black", label=r"$\omega_p^2/(gT)^2$")

# Labels and Positioning
plt.text(2.2, 1.7, r"$f_g^2$", fontsize=12)
plt.text(1.5, 0.75, r"$\alpha_s$", fontsize=12)
plt.text(2.5, 0.28, r"$\omega_p^2/(g T)^2$", fontsize=12)

plt.xlim(0.5, 5.0)
plt.ylim(0.0, 2.0)
plt.xlabel(r"$T/T_c$", fontsize=12)
plt.xticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], 
           ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"])

plt.tight_layout()
plt.show()