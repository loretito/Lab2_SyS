from def_signals import * 

def calc_energy_average_power(t):

    # Cálculo de energía y potencia media
    signals = [senoidal, cuadratica, diente_de_sierra, triangular, exponencial_decreciente, exponencial_creciente, impulso, u, sinc]
    names = ['Senoidal', 'Cuadrada', 'Diente de Sierra', 'Triangular', 'Exponencial Decreciente', 'Exponencial Creciente', 'Impulso', 'Escalón Unitario', 'Sinc']

    for signal, name in zip(signals, names):
        energy = np.sum(np.abs(signal(t))**2) 
        power = np.sum(np.abs(signal(t))**2) 
        print(f'== {name} ==\nEnergía: {energy:.2f}\nPotencia Media: {power:.2f}\n\n')
