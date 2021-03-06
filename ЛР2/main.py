from math import cos, sin, atan, tan, radians, fabs, sqrt, pi
import math
import numpy as np

# КОНСТАНТЫ
# -----------------------------------
μ = 398603
R = 6371
# -----------------------------------


# ИСХОДНЫЕ ДАННЫЕ
# -----------------------------------
apocenter_height = 350  # Hа
pericenter_height = 240  # Hп
mood = radians(10)  # i
ascending_node_longitude = radians(5)  # 𝛀
pericenter_argument = radians(0)  # ω
mean_anomaly = radians(60)  # M
# -----------------------------------


get_a = lambda ra, rp: 0.5 * (ra + rp)
get_e = lambda ra, rp, a: (ra - rp) / (2 * a)
get_theta = lambda e, E: 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2))
get_r = lambda a, e, E: a * (1 - e * cos(E))

get_p = lambda a, e: a * (1 - e ** 2)
get_Vr = lambda p, theta, e: sqrt(μ / p) * e * sin(theta)
get_Vt = lambda p, theta, e: sqrt(μ / p) * (1 + e * cos(theta))


def get_agesk(theta, ra, i, big_omega, omega):
    X = ra * (cos(omega + theta) * cos(big_omega) - sin(theta + omega) * sin(big_omega) * cos(i))
    Y = ra * (cos(omega + theta) * sin(big_omega) + sin(theta + omega) * cos(big_omega) * cos(i))
    Z = ra * sin(omega + theta) * sin(i)
    return X, Y, Z


def find_E(e, M, error=1e-3):
    E1 = M
    E2 = M + e * sin(E1)
    while fabs(E2 - E1) > error:
        E1 = E2
        E2 = M + e * sin(E1)
    return E1


a = get_a(ra=R + apocenter_height, rp=R + pericenter_height)
e = get_e(ra=R + apocenter_height, rp=R + pericenter_height, a=a)
E = find_E(e=e, M=mean_anomaly)
theta = get_theta(e=e, E=E)
Ra = get_r(a=a, e=e, E=E)

print('a =', a)
print('e =', e)
print('E =', math.degrees(E))
print('theta =', math.degrees(theta))
print('Ra =', Ra)

Xa, Ya, Za = get_agesk(theta=theta, ra=Ra, i=mood, big_omega=ascending_node_longitude, omega=pericenter_argument)

AGESK_COORD = np.array([
    [Xa],
    [Ya],
    [Za]
])

print(AGESK_COORD)


def get_transition_matrix(S):
    matrix = np.array([
        [cos(S), sin(S), 0],
        [-sin(S), cos(S), 0],
        [0, 0, 1],
    ])
    return matrix


T = 86164.090530833  # seconds
Rate = 2 * pi / T

COORD1 = get_transition_matrix(0).dot(AGESK_COORD)
COORD2 = get_transition_matrix(pi).dot(AGESK_COORD)

a = 6378136 / 1e3
ez_sqr = 0.0067385254

heights = []

for coord in [COORD1, COORD2]:
    x, y, z = coord[0][0], coord[1][0], coord[2][0]
    D = math.hypot(x, y)
    B, L, H = 0, 0, 0

    if D == 0:
        B = pi / 2 * z / fabs(z)
        L = 0
        H = z * sin(B) - a * sqrt(1 - ez_sqr * sin(B) ** 2)
        print(B, L, H)

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

    heights.append(H)

get_density = lambda density_H, K0, K1, K2, K3, K4: density_H * K0 * (1 + K1 + K2 + K3 + K4)


def get_density_H(H, a0, a1, a2, a3, a4, a5, a6):
    density_0 = 1.58868 * 1e-8
    power_value = a0 + a1 * H + a2 * pow(H, 2) + a3 * pow(H, 3) + a4 * pow(H, 4) + a5 * pow(H, 5) + a6 * pow(H, 6)
    return density_0 * math.exp(power_value)
