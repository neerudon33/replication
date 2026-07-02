import numpy as np
import matplotlib.pyplot as plt

from .coupling import alpha_s
def plot_alpha():

    temperature = np.linspace(0.84,5,500)

    alpha = alpha_s(temperature)

   



   

def plot_fg2(temperature, fg2_values):

    plt.figure(figsize=(8,5))

    plt.plot(
        temperature,
        fg2_values,
        linewidth=2,
        label=r"$f_g^2$"
    )

    plt.xlabel(r"$T/T_c$")
    plt.ylabel(r"$f_g^2$")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()

def plot_figure2(temperature, fg2_values, omega):

    alpha = alpha_s(temperature)

    plt.figure(figsize=(8,6))

    # fg²
    plt.plot(
        temperature,
        fg2_values,
        linestyle='-.',
        linewidth=2,
        color='red',
        label=r'$f_g^2$'
    )

    # alpha_s
    plt.plot(
        temperature,
        alpha,
        linestyle='--',
        linewidth=2,
        color='blue',
        label=r'$\alpha_s$'
    )

    # omega²/(g²T²)
    plt.plot(
        temperature,
        omega,
        linestyle='-',
        linewidth=2,
        color='green',
        label=r'$\omega_p^2/(g^2T^2)$'
    )

    plt.xlim(0.5,5)

    plt.ylim(0,2)

    plt.xlabel(r'$T/T_c$',fontsize=14)

    plt.grid(False)

    plt.legend()

    plt.tight_layout()

    plt.show()