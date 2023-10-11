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

