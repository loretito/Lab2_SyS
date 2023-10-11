# # Convolución
from def_signals import *
import matplotlib.pyplot as plt

entry_signals = [senoidal, cuadratica, triangular, diente_de_sierra, senoidal]
e_name = ["Senoidal", "Cuadrada", "Triangular", "Diente de Sierra", "Senoidal"]

h_signals = [exponencial_decreciente, exponencial_creciente, impulso, u, sinc]
h_name = ["Exponencial Decreciente", "Exponencial Creciente", "Impulso", "Escalón Unitario", "Sinc"]

h_signals2 = [diente_de_sierra, triangular, cuadratica, senoidal, cuadratica]
h_name2 = ["Diente de Sierra", "Triangular", "Cuadrada", "Senoidal", "Cuadrada"] 

def convolution1(t):
    for xt, ht, xname, hname in zip(entry_signals, h_signals, e_name, h_name):
        convoluted_signal = np.convolve(xt(t), ht(t), "same") / len(t)

        show_convolution(t, xt, ht, convoluted_signal, xname, hname)
        
def convolution2(t):
    for xt, ht, xname, hname in zip(h_signals, h_signals2, h_name, h_name2):
        convoluted_signal = np.convolve(xt(t), ht(t), "same") / len(t)

        show_convolution(t, xt, ht, convoluted_signal, xname, hname)        


def show_convolution(t, xt, ht, convoluted_signal, xname, hname):
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    # Graficar x(t)
    axs[0].plot(t, xt(t), label="x(t)")
    axs[0].set_title(f"x(t) = {xname}")
    axs[0].set_ylabel("x(t)")
    axs[0].grid(True)

    # Graficar h(t)
    h_values = ht(t) if callable(ht) else ht
    axs[1].plot(t, h_values, label="h(t)")
    axs[1].set_title(f"h(t) = {hname}")
    axs[1].set_ylabel("h(t)")
    axs[1].grid(True)

    # Graficar y(t) = convolución
    axs[2].plot(t, convoluted_signal, label="y(t)")
    axs[2].set_title(f"Convolución ({xname} * {hname})")
    axs[2].set_xlabel("t")
    axs[2].set_ylabel("y(t)")
    axs[2].grid(True)

    # Ajustar el layout
    plt.tight_layout()
    plt.show()


k_arr = [2, 3, 4, -2, -1]
tau_arr = [4, -2, 5, 1, 2]


def fp_and_ct(t):
    for k, tau, xt, ht, xname, hname in zip(k_arr, tau_arr, entry_signals, h_signals, e_name, h_name):
        h_t = k * ht(t - tau)
        convoluted_signal = np.convolve(xt(t), h_t, "same") / len(t)

        show_convolution(t, xt, h_t, convoluted_signal, xname, hname)
