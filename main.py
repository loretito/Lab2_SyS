import numpy as np
import matplotlib.pyplot as plt

# Definición de señales

def senoidal(t):
    return np.sin(2 * np.pi * t)

def cuadratica(t):
    return np.sign(np.sin(np.pi * t))

def diente_de_sierra(t):
    return t - np.floor(t)

def triangular(t):
    return 2 * np.abs(diente_de_sierra(t) - 0.5)

def exponencial_decreciente(t):
    return np.exp(-t) * (u(t) - u(t-1))

def exponencial_creciente(t):
    return np.exp(t) * (u(t) - u(t-1))

def impulso(t):
    return np.where(t == 0, 1, 0)

def u(t):
    return np.where(t >= 0, 1, 0)

def sinc(t):
    return np.where(t == 0, 1, np.sin(t)/t)

# Parámetros
t = np.linspace(-5, 5, 10001)
dt = t[1] - t[0]

# Cálculo de energía y potencia media
signals = [senoidal, cuadratica, diente_de_sierra, triangular, exponencial_decreciente, exponencial_creciente, impulso, u, sinc]
names = ['Senoidal', 'Cuadrada', 'Diente de Sierra', 'Triangular', 'Exponencial Decreciente', 'Exponencial Creciente', 'Impulso', 'Escalón Unitario', 'Sinc']

for signal, name in zip(signals, names):
    energy = np.sum(np.abs(signal(t))**2) * dt
    power = np.mean(np.abs(signal(t))**2) / len(t)
    print(f'{name} - Energía: {energy:.2f}, Potencia Media: {power:.2f}')

# Graficar señales
plt.figure(figsize=(15, 10))

plt.subplot(3, 3, 1)
plt.plot(t, senoidal(t))
plt.title('Senoidal')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 2)
plt.plot(t, cuadratica(t))
plt.title('Cuadrada')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 3)
plt.plot(t, diente_de_sierra(t))
plt.title('Diente de Sierra')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 4)
plt.plot(t, triangular(t))
plt.title('Triangular')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 5)
plt.plot(t, exponencial_decreciente(t))
plt.title('Exponencial Decreciente')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 6)
plt.plot(t, exponencial_creciente(t))
plt.title('Exponencial Creciente')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 7)
plt.plot(t, impulso(t))
plt.title('Impulso')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 8)
plt.plot(t, u(t))
plt.title('Escalón')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.subplot(3, 3, 9)
plt.plot(t, sinc(t))
plt.title('Sinc')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.tight_layout()
plt.show()

# Convolución

# senoidal y expoencial decreciente
convoluted_signal = np.convolve(senoidal(t), exponencial_decreciente(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, senoidal(t), label='x(t)')
axs[0].set_title('x(t) = Senoidal')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, exponencial_decreciente(t), label='h(t)')
axs[1].set_title('h(t) = Expoencial Decreciente')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Senoidal * Exponencial Decreciente)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# cuadrada y exponencial creciente
convoluted_signal = np.convolve(cuadratica(t), exponencial_creciente(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, cuadratica(t), label='x(t)')
axs[0].set_title('x(t) = Cuadrada')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, exponencial_creciente(t), label='h(t)')
axs[1].set_title('h(t) = Exponencial Creciente')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Cuadrada * Exponencial Creciente)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# triangular y impulso unitario
convoluted_signal = np.convolve(triangular(t), impulso(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, triangular(t), label='x(t)')
axs[0].set_title('x(t) = Triangular')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, impulso(t), label='h(t)')
axs[1].set_title('h(t) = Impulso Unitario')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Triangular * Impulso Unitario)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()


# diente de sierra y escalon unitario
convoluted_signal = np.convolve(diente_de_sierra(t), u(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, diente_de_sierra(t), label='x(t)')
axs[0].set_title('x(t) = Diente de Sierra')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, u(t), label='h(t)')
axs[1].set_title('h(t) = Escalón Unitario')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Diente de Sierra * Escalón Unitario)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# senoidal y sinc

convoluted_signal = np.convolve(senoidal(t), sinc(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, senoidal(t), label='x(t)')
axs[0].set_title('x(t) = Senoidal')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, sinc(t), label='h(t)')
axs[1].set_title('h(t) = Sinc')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución ( Senoidal * Sinc)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()


## CORRIMIENTO TEMPORAL Y FACTOR DE PROPORCION

# senoidal y expoencial decreciente
k = 2
tau = 4

h_t = k * exponencial_decreciente(t - tau)
convoluted_signal = np.convolve(senoidal(t), h_t, 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, senoidal(t), label='x(t)')
axs[0].set_title('x(t) = Senoidal')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, h_t, label='h(t)')
axs[1].set_title('h(t) = Exponencial Decreciente')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Senoidal * Exponencial Decreciente)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# cuadrada y exponencial creciente

k = 3
tau = -2

h_t = k * exponencial_creciente(t - tau)

convoluted_signal = np.convolve(cuadratica(t), h_t, 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, cuadratica(t), label='x(t)')
axs[0].set_title('x(t) = Cuadrada')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, h_t, label='h(t)')
axs[1].set_title('h(t) = Exponencial Creciente')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Cuadrada * Exponencial Creciente)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# triangular y impulso unitario
k = 4
tau = 5

h_t = k * impulso(t - tau)

convoluted_signal = np.convolve(triangular(t), h_t, 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, triangular(t), label='x(t)')
axs[0].set_title('x(t) = Triangular')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, h_t, label='h(t)')
axs[1].set_title('h(t) = Impulso Unitario')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Triangular * Impulso Unitario)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()


# diente de sierra y escalon unitario
k = -2
tau = 1

h_t = k * u(t - tau)
convoluted_signal = np.convolve(diente_de_sierra(t), h_t, 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, diente_de_sierra(t), label='x(t)')
axs[0].set_title('x(t) = Diente de Sierra')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, h_t, label='h(t)')
axs[1].set_title('h(t) = Escalón Unitario')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Diente de Sierra * Escalón Unitario)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# senoidal y sinc
k = -1
tau = 2

h_t = k * sinc(t - tau)
convoluted_signal = np.convolve(senoidal(t), h_t, 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, senoidal(t), label='x(t)')
axs[0].set_title('x(t) = Senoidal')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, h_t, label='h(t)')
axs[1].set_title('h(t) = Sinc')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución ( Senoidal * Sinc)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()






# exponencial decreciente con diente de sierra
convoluted_signal = np.convolve(exponencial_decreciente(t), diente_de_sierra(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, exponencial_decreciente(t), label='x(t)')
axs[0].set_title('x(t) = Exponencial Decreciente')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, diente_de_sierra(t), label='h(t)')
axs[1].set_title('h(t) = Diente de Sierra')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Exp. Decreciente * Diente de Sierra)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# expoencial creciente con triangular
convoluted_signal = np.convolve(exponencial_creciente(t), triangular(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, exponencial_creciente(t), label='x(t)')
axs[0].set_title('x(t) = Exponential Creciente')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, triangular(t), label='h(t)')
axs[1].set_title('h(t) = Triangular')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Exponencial Creciente * Triangular)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# impulso unitario con cuadrada
convoluted_signal = np.convolve(impulso(t), cuadratica(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, impulso(t), label='x(t)')
axs[0].set_title('x(t) = Impulso Unitario')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, cuadratica(t), label='h(t)')
axs[1].set_title('h(t) = Cuadrada')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Impulso Unitario * Cuadrada)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()


#  escalon unitario con senoidal
convoluted_signal = np.convolve(u(t), senoidal(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, u(t), label='x(t)')
axs[0].set_title('x(t) = Escalón Unitario')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, senoidal(t), label='h(t)')
axs[1].set_title('h(t) = Senoidal')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución (Escalón Unitario * Senoidal)')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()

# sinc con cuadrada

convoluted_signal = np.convolve(sinc(t), cuadratica(t), 'same') / len(t)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Graficar x(t) 
axs[0].plot(t, sinc(t), label='x(t)')
axs[0].set_title('x(t) = Sinc')
axs[0].set_ylabel('x(t)')
axs[0].grid(True)

# Graficar h(t)
axs[1].plot(t, cuadratica(t), label='h(t)')
axs[1].set_title('h(t) = Cuadrada')
axs[1].set_ylabel('h(t)')
axs[1].grid(True)

# Graficar y(t) = convolución 
axs[2].plot(t, convoluted_signal, label='y(t)')
axs[2].set_title('Convolución ( Sinc * Cuadrada )')
axs[2].set_xlabel('t')
axs[2].set_ylabel('y(t)')
axs[2].grid(True)

# Ajustar el layout
plt.tight_layout()
plt.show()