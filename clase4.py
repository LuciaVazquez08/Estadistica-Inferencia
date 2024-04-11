import numpy as np
import matplotlib.pyplot as plt

def simular_cobertura(p, n, alfa):
    intervalos_confianza = []
    for i in range(1, n+1):
        exitos = np.random.binomial(i,p,i) 
        intervalo = ((estimar_p(exitos, i) - epsilon_n(i, alfa)) <= p ) and (p <= (estimar_p(exitos, i) + epsilon_n(i, alfa)))
        intervalos_confianza.append(intervalo)
    return intervalos_confianza

def graficar_simulacion(p, n, alfa):
    intervalos = simular_cobertura(p,n,alfa)
    proporcion = np.cumsum(intervalos) / np.arange(1, n+1)
    plt.plot(np.arange(1, n + 1), proporcion)
    plt.xlabel('n')
    plt.ylabel('Intervalo de confianza')
    plt.title(f'Intervalo de confianza vs n for p={p}, alpha={alfa}')
    plt.show()

def calcular_intervalo(alfa, n):
    return epsilon_n(n, alfa) * 2


def graficar_longitud_intervalo(alpha, max_length):
    n_values = []
    interval_lengths = []
    flag = True
    n = 1
    while flag:
        interval_length = calcular_intervalo(alpha, n)
        n_values.append(n)
        interval_lengths.append(interval_length)
        if interval_length >= max_length:
            flag = False
        n += 1
    plt.plot(n_values, interval_lengths)
    plt.xlabel('n')
    plt.ylabel('Interval Length')
    plt.title(f'Interval Length vs n for alpha={alpha}')
    plt.show()

def calcular_n(max_valor_intervalo, alfa):
    n = 1
    flag = True
    while flag:
        interval_length = calcular_intervalo(alfa, n)
        if interval_length >= max_valor_intervalo:
            flag = False
        n += 1
    return n


def estimar_p(exitos, n):
    return np.mean(exitos) / n

def epsilon_n(n, alfa):
    return np.sqrt((1 / (2 * n)) * np.log(2 / alfa))

# Ejemplo de uso
p = 0.4
alfa = 0.05
n_max = 10000

# (a) Graficar la cobertura
graficar_simulacion(p, n_max, alfa)

# (b) Graficar la longitud del intervalo versus n para max_length = 0.05
graficar_longitud_intervalo(alfa, 0.05)