"""moon.py
Здесь описаны основные характеристики Луны, её орбиты,
а также возмущения действующие на спутник со стороны луны

Данные взяты с https://ru.wikipedia.org/wiki/%D0%9B%D1%83%D0%BD%D0%B0


Элементы орбиты земли, такие как долгота восходящего узла и аргуемент перицентра
взяты с http://www.spacephys.ru/ugly-orbity-luny за 2021 год
"""

import math
import functions

# Орбитильные характристики
# ====================================
perigee = 363_104  # km
apogee = 405_696  # km
a = 384_399  # km
e = 0.0549
T = 27.321661 * 24  # hour
i = math.radians(23.25)  # radians
orbital_speed = 1.023 * 3600  # km/h

OMEGA = math.radians(10.86)
omega = math.radians(206.41)
# ====================================


# Физические характристики
# ===========================
mass = 7.3477e22  # kg
moon_f = 4900.8 * (3600 * 3600)  # km^3/hour^-2
# moon_f = 4900.8  # km^3/hour^-2
moon_radius = 1737.10  # km


# ===========================


def find_moon_position(t):
    n = math.sqrt(moon_f / (a ** 3))
    M = math.radians(275.5) + n * t
    # print(M)
    E = -10
    dE = 1e-3
    error = 1e-2
    # print('M',M,'t',t)
    while math.fabs(E - e * math.sin(E) - M) > error:
        E += dE

    theta = 2 * math.atan(math.sqrt((1 + e) / (1 - e)) * math.tan(E / 2))
    theta = 2 * math.pi + theta if theta < 0 else theta
    # print('t', t, 'theta', theta)

    p = functions.get_p(a=a, e=e)
    r = functions.get_r(p=p, e=e, theta=theta)
    coord = functions.get_agesk(theta=theta, ra=r, i=i, big_omega=OMEGA, omega=omega)

    return coord, theta


# moon_coord 		- кортеж формата (x, y, z)
# spacecraft_coord 	- кортеж формата (x, y, z)
# spacecraft_mass 	- скаляр
def find_moon_STW(moon_coord, spacecraft_coord, theta):
    X, Y, Z = moon_coord
    x, y, z = spacecraft_coord
    rM = math.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    r0 = math.sqrt((X - x) ** 2 + (Y - y) ** 2 + (Z - z) ** 2)

    Fx = moon_f * (X - x) / r0 ** 3 - moon_f * X / rM ** 3
    Fy = moon_f * (Y - y) / r0 ** 3 - moon_f * Y / rM ** 3
    Fz = moon_f * (Z - z) / r0 ** 3 - moon_f * Z / rM ** 3

    S = Fx * math.cos(theta) + Fy * math.sin(theta)
    T = -Fx * math.sin(theta) + Fy * math.cos(theta)
    W = Fz

    return S, T, W


def test(hours):
    x = []
    y = []
    z = []
    for t in range(hours):
        _x, _y, _z = find_moon_position(t=t)
        x.append(_x)
        y.append(_y)
        z.append(_z)

    import matplotlib.pyplot as plt
    import data
    s = [1] * len(x)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=s)
    ax.scatter(x[0], y[0], z[0], s=25, color='orange')
    ax.scatter(x[-1], y[-1], z[-1], s=25, color='red')
    ax.scatter([0], [0], [0], s=data.Earth_radius, color='green')
    plt.show()


if __name__ == '__main__':
    test(24 * 365 // 2)
