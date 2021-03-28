import math
from AtmosphericDensityModelCoefficients import *
from data import *
from math import cos, sin, atan, tan, radians, fabs, sqrt, pi
import numpy as np

# Формулы для рассчёта компонентов возмущающего ускорения,
# вызванного нецентральность гравитационного поля Земли
# ===================================================================================
Epsilon = 398603 * 66.07 * 1e3
S1 = lambda r, i, u: Epsilon / r ** 4 * (3 * math.sin(i) ** 2 * math.sin(u) ** 2 - 1)
T1 = lambda r, i, u: -Epsilon / r ** 4 * math.sin(i) ** 2 * math.sin(2 * u)
W1 = lambda r, i, u: -Epsilon / r ** 4 * math.sin(2 * i) * math.sin(u)

S2 = lambda sigma_x, density, V, Vr: -sigma_x * density * V * Vr
T2 = lambda sigma_x, density, V, Vt: -sigma_x * density * V * Vt
W2 = 0
# ===================================================================================

# Правые части диф уравнений метода оскулирующих элементов
# =====================================================================================================================
R_p = lambda r, T, F: 2 * r * T * F

R_OMEGA = lambda W, F, r, p, u, i: W * F * r / p * math.sin(u) / math.sin(i)

R_i = lambda W, F, r, p, u: W * F * r / p * math.cos(u)

R_omega = lambda F, S, theta, e, T, r, p, W, i, u: F * (
        -S * math.cos(theta) / e + T * (1 + r / p) * math.sin(theta) / e - W * r / p * (1 / math.tan(i)) * math.sin(u))

R_e = lambda F, S, theta, T, r, p, e: F * (S * math.sin(theta) + T * ((1 + r / p) * math.cos(theta) + e * r / p))

R_tau = lambda F, p: F * math.sqrt(398603 / p)

geT_F = lambda r, S, T, theta, e, p: (398603 / r ** 2 + S * math.cos(theta) / e - T * (1 + r / p) * math.sin(
    theta) / e) ** -1
# =====================================================================================================================

# Вспомогательные функции
# ========================================================
get_a = lambda ra, rp: 0.5 * (ra + rp)
get_e = lambda ra, rp, a: (ra - rp) / (2 * a)
get_r = lambda p, e, theta: p / (1 + e * math.cos(theta))
get_p = lambda a, e: a * (1 - e ** 2)
get_Vr = lambda p, theta, e: sqrt(398603 / p) * e * sin(theta)
get_Vt = lambda p, theta, e: sqrt(398603 / p) * (1 + e * cos(theta))
# ========================================================

get_sigma_x = lambda Cxa, Sa, m: Sa * Cxa / (2 * m)


def get_t_from_tau(tau, theta, p, e):
    f = lambda angle: 1 / (1 + e * math.cos(angle)) ** 2
    d_theta = 1e-2
    theta1 = 0
    sum = 0
    while theta1 < theta:
        sum += d_theta * f(angle=theta1 + 0.5 * d_theta)
        theta1 += d_theta

    sum *= math.sqrt(p / 398603)
    sum += tau
    return sum


# Функция для получеения АГЭСК координат
def get_agesk(theta, ra, i, big_omega, omega):
    X = ra * (cos(omega + theta) * cos(big_omega) - sin(theta + omega) * sin(big_omega) * cos(i))
    Y = ra * (cos(omega + theta) * sin(big_omega) + sin(theta + omega) * cos(big_omega) * cos(i))
    Z = ra * sin(omega + theta) * sin(i)
    return X, Y, Z


# Функция для получения матрицы взаимного перехода (АГЭСК -> ГСК)
def get_transition_matrix(S):
    matrix = np.array([
        [cos(S), sin(S), 0],
        [-sin(S), cos(S), 0],
        [0, 0, 1],
    ])
    return matrix


def find_H(Ra, theta, i, big_omega, omega, p, e, tau):
    # АГЭСК
    # ===============================================================================================================
    Xa, Ya, Za = get_agesk(theta=theta, ra=Ra, i=i, big_omega=big_omega, omega=omega)
    AGESK_COORD = np.array([[Xa], [Ya], [Za]])
    # ===============================================================================================================

    rate = 7.292115855306578e-05
    t = get_t_from_tau(tau=tau, theta=theta, p=p, e=e)
    # ГСК
    # =================================================
    coord = get_transition_matrix(rate * t).dot(AGESK_COORD)
    # =================================================

    a = 6378.136
    ez_sqr = 0.0067385254
    # Поиск B, L, H
    # ==========================================================
    x, y, z = coord[0][0], coord[1][0], coord[2][0]
    D = math.hypot(x, y)
    B, L, H = 0, 0, 0
    if D == 0:
        B = pi / 2 * z / fabs(z)
        L = 0
        H = z * sin(B) - a * sqrt(1 - ez_sqr * sin(B) ** 2)
    else:
        La = math.asin(y / D)
        if y < 0 and x > 0: L = 2 * pi - La
        if y < 0 and x < 0: L = pi + La
        if y > 0 and x < 0: L = pi - La
        if y > 0 and x > 0: L = La
        if z == 0:
            B = 0
            H = D - a
        else:
            r = sqrt(x ** 2 + y ** 2 + z ** 2)
            c = math.asin(z / r)
            p = (ez_sqr * a) / (2 * r)
            s1 = 0
            b = c + s1
            s2 = math.asin((p * sin(2 * b)) / sqrt(1 - ez_sqr * sin(b) ** 2))
            while not fabs(s2 - s1) < 1e-3:
                s1 = s2
                b = c + s1
                s2 = math.asin((p * sin(2 * b)) / sqrt(1 - ez_sqr * sin(b) ** 2))
            B = b
            H = D * cos(B) + z * sin(B) - a * sqrt(1 - ez_sqr * sin(B) ** 2)

    return H
    # ==========================================================


def find_density(H):
    table = None

    if 120 <= H <= 500:
        table = table1

    if 500 < H:
        if H > 1500:
            print(f'WARNING H={H}')
        table = table2

    index = table['F0'].index(Fa)

    a0 = table['a0'][index]
    a1 = table['a1'][index]
    a2 = table['a2'][index]
    a3 = table['a3'][index]
    a4 = table['a4'][index]
    a5 = table['a5'][index]
    a6 = table['a6'][index]

    density_H = get_density_H(H=H, a0=a0, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6)
    return get_density(density_H=density_H)


# Функция для вычисления плотности атмосферы
def get_density(density_H, K0=1, K1=0, K2=0, K3=0, K4=0):
    return density_H * K0 * (1 + K1 + K2 + K3 + K4)


# Функция для вычисления плотности ночной атмосферы
def get_density_H(H, a0, a1, a2, a3, a4, a5, a6):
    density_0 = 1.58868 * 1e-8
    power_value = a0 + a1 * H + a2 * pow(H, 2) + a3 * pow(H, 3) + a4 * pow(H, 4) + a5 * pow(H, 5) + a6 * pow(H, 6)
    return density_0 * math.exp(power_value)
