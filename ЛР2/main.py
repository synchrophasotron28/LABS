from math import cos, sin, atan, tan, radians, fabs, sqrt

# КОНСТАНТЫ
# -----------------------------------
μ = 398603
R = 6371
# -----------------------------------


# ИСХОДНЫЕ ДАННЫЕ
# -----------------------------------
apocenter_height = 350  # Rа
pericenter_height = 240  # Rп
mood = radians(10)  # i
ascending_node_longitude = radians(5)  # 𝛀
pericenter_argument = radians(0)  # ω
mean_anomaly = radians(60)  # M
# -----------------------------------


get_a = lambda ra, rp: 0.5 * (ra + rp)
get_e = lambda ra, rp, a: (ra - rp) / (2 * a)
get_theta = lambda e, E: 2 * atan(((1 + e) / (1 - e)) * tan(E / 2))
get_r = lambda a, e, E: a * (1 - e * cos(E))

get_p = lambda a, e: a * (1 - e ** 2)
get_Vr = lambda p, theta, e: sqrt(μ / p) * e * sin(theta)
get_Vt = lambda p, theta, e: sqrt(μ / p) * (1 + e * cos(theta))


def get_agesk(theta, ra, i, big_omega, omega):
    X = ra * (cos(omega + theta) * cos(big_omega) - sin(theta + omega) * sin(big_omega) * cos(i))
    Y = ra * (cos(omega + theta) * sin(big_omega) + sin(theta + omega) * cos(big_omega) * cos(i))
    Z = ra * sin(omega + theta)
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

Xa, Ya, Za = get_agesk(theta=theta, ra=Ra, i=mood, big_omega=ascending_node_longitude, omega=pericenter_argument)

print(Xa, Ya, Za)
