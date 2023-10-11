import matplotlib.pyplot as plt

from def_signals import *

# Graficar señales
def show(t):
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 3, 1)
    plt.plot(t, senoidal(t))
    plt.title('Senoidal')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 2)
    plt.plot(t, cuadratica(t))
    plt.title('Cuadrada')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 3)
    plt.plot(t, diente_de_sierra(t))
    plt.title('Diente de Sierra')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 4)
    plt.plot(t, triangular(t))
    plt.title('Triangular')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 5)
    plt.plot(t, exponencial_decreciente(t))
    plt.title('Exponencial Decreciente')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 6)
    plt.plot(t, exponencial_creciente(t))
    plt.title('Exponencial Creciente')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 7)
    plt.plot(t, impulso(t))
    plt.title('Impulso')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 8)
    plt.plot(t, u(t))
    plt.title('Escalón')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.subplot(3, 3, 9)
    plt.plot(t, sinc(t))
    plt.title('Sinc')
    plt.xlabel('n')
    plt.ylabel('x[n]')

    plt.tight_layout()
    plt.show()
    
    print("\n\n")
