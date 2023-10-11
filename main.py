import numpy as np

from def_signals import *
from show_signals import *
from energy_avg_power import *
from convolution import *

# Parámetros
t = np.linspace(-5, 5, 10001)

# Mostrar las señales periodicas y aperiódicas
show(t)

# Calcular energía y potencia media
calc_energy_average_power(t)

# Realizar la convolucion de señales periodicas y aperiódicas
convolution1(t)

# Aplicar factor de escala y desplazamiento temporal
fp_and_ct(t)

#Realizar la convolucion de señales aperiodicas y periódicas
convolution2(t)
