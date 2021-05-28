from math import cos, sin, atan, tan, radians, fabs, sqrt, pi
import math
import numpy as np
import matplotlib.pyplot as plt
from constant_data import *

Earth_gravity_potential = 698603 * 3600 * 3600

# Вспомогательные функции
# ========================================================
get_a = lambda ra, rp: 0.5 * (ra + rp)
get_e = lambda ra, rp, a: (ra - rp) / (2 * a)
get_r = lambda p, e, theta: p / (1 + e * math.cos(theta))
get_p = lambda a, e: a * (1 - e ** 2)
get_Vr = lambda p, theta, e: sqrt(Earth_gravity_potential / p) * e * sin(theta)
get_Vt = lambda p, theta, e: sqrt(Earth_gravity_potential / p) * (1 + e * cos(theta))

# ========================================================

# Правые части диф уравнений метода оскулирующих элементов
# =====================================================================================================================
R_p = lambda r, T, F: 2 * r * T * F

R_OMEGA = lambda W, F, r, p, u, i: W * F * r / p * math.sin(u) / math.sin(i)

R_i = lambda W, F, r, p, u: W * F * r / p * math.cos(u)

R_omega = lambda F, S, theta, e, T, r, p, W, i, u: F * (
        -S * math.cos(theta) / e + T * (1 + r / p) * math.sin(theta) / e - W * r / p * (1 / math.tan(i)) * math.sin(u))

R_e = lambda F, S, theta, T, r, p, e: F * (S * math.sin(theta) + T * ((1 + r / p) * math.cos(theta) + e * r / p))

R_tau = lambda F, p: F * math.sqrt(Earth_gravity_potential / p)

geT_F = lambda r, S, T, theta, e, p: (Earth_gravity_potential / r ** 2 + S * math.cos(theta) / e - T * (
        1 + r / p) * math.sin(
    theta) / e) ** -1


# =====================================================================================================================

# Функция для получеения АГЭСК координат
def get_agesk(theta, ra, i, big_omega, omega):
    X = ra * (cos(omega + theta) * cos(big_omega) - sin(theta + omega) * sin(big_omega) * cos(i))
    Y = ra * (cos(omega + theta) * sin(big_omega) + sin(theta + omega) * cos(big_omega) * cos(i))
    Z = ra * sin(omega + theta) * sin(i)
    return X, Y, Z


# Функция для поиска эксцентрической аномалии Е
def find_E(e, M, error=1e-3):
    E1 = M
    E2 = M + e * sin(E1)
    while fabs(E2 - E1) > error:
        E1 = E2
        E2 = M + e * sin(E1)
    return E1


# Функция для получения матрицы взаимного перехода (АГЭСК -> ГСК)
def get_transition_matrix(S):
    matrix = np.array([
        [cos(S), sin(S), 0],
        [-sin(S), cos(S), 0],
        [0, 0, 1],
    ])
    return matrix


# Функция для вычисления плотности атмосферы
def get_density(density_H, K0, K1, K2, K3, K4):
    return density_H * K0 * (1 + K1 + K2 + K3 + K4)


# Функция для вычисления плотности ночной атмосферы
def get_density_H(H, a0, a1, a2, a3, a4, a5, a6):
    density_0 = 1.58868 * 1e-8
    power_value = a0 + a1 * H + a2 * pow(H, 2) + a3 * pow(H, 3) + a4 * pow(H, 4) + a5 * pow(H, 5) + a6 * pow(H, 6)
    return density_0 * math.exp(power_value)


# Функция для построения графиков
def build_chart(title, xlabel, ylabel, x_data, y_data):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x_data, y_data,
             marker='.', markersize=20,
             color='blue',
             markerfacecolor='orange')
    plt.plot(x_data, y_data, linewidth=1)
    plt.grid()
    plt.savefig('./charts/{}.png'.format(title.split(' ')[0]))
    plt.show()
