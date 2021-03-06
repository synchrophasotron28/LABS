from AtmosphericDensityModelCoefficients import table1
from functions import *
from constant_data import *

# большая полуось(а)
# эксцентриситет(е)
# эксцентрическая аномалия(E)
# истинная аномалия(theta)
# модуль радиус-вектора КА в АГЭСК(Ra)
# ===============================================================
a = get_a(ra=R + apocenter_height, rp=R + pericenter_height)
e = get_e(ra=R + apocenter_height, rp=R + pericenter_height, a=a)
E = find_E(e=e, M=mean_anomaly)
theta = get_theta(e=e, E=E)
Ra = get_r(a=a, e=e, E=E)
# ===============================================================

# фокальный параметр (p)
# радиальная составляющая вектора скорости (Vr)
# трансверсальная составляющая вектора скорости (Vr)
# модуль веткора скорости (V)
# ==================================================
p = get_p(a=a, e=e)
Vr = get_Vr(p=p, theta=theta, e=e)
Vt = get_Vt(p=p, theta=theta, e=e)
V = math.hypot(Vr, Vt)
# ==================================================

# АГЭСК
# ===============================================================================================================
Xa, Ya, Za = get_agesk(theta=theta, ra=Ra, i=mood, big_omega=ascending_node_longitude, omega=pericenter_argument)
AGESK_COORD = np.array([[Xa], [Ya], [Za]])
# ===============================================================================================================

# ГСК
# =================================================
COORD1 = get_transition_matrix(0).dot(AGESK_COORD)
COORD2 = get_transition_matrix(pi).dot(AGESK_COORD)
# =================================================

heights = []
a = 6378.136

# Поиск B, L, H
# ==========================================================
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
# ==========================================================

# Расчёт плотности при разных уровнях солнечной активности
# =====================================================================================
density_table = []
for h in heights:
    table = None
    if 120 <= h <= 500:
        table = table1
    density_table.clear()
    for column in range(len(table['F0'])):
        F0 = table['F0'][column]
        a0 = table['a0'][column]
        a1 = table['a1'][column]
        a2 = table['a2'][column]
        a3 = table['a3'][column]
        a4 = table['a4'][column]
        a5 = table['a5'][column]
        a6 = table['a6'][column]

        density_H = get_density_H(H=h, a0=a0, a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6)
        density = get_density(density_H=density_H, K0=1, K1=0, K2=0, K3=0, K4=0)
        density /= 1e-9
        density_table.append((F0, density))
# =====================================================================================

# Вычисление S, T, W
# ========================================
S_list = []
T_list = []
W_list = []
F0_list = [i[0] for i in density_table]
for F0, density in density_table:
    S = -1 * SIGMA_X * density * V * Vr
    T = -1 * SIGMA_X * density * V * Vt
    W = 0

    S_list.append(S)
    T_list.append(T)
    W_list.append(W)
# ========================================

H = round(H, 2)

# Построение графиков
# =========================================================================================================================
build_chart(title=f'ρ(F0), H={H} km', xlabel='F0', ylabel='ρ', x_data=F0_list, y_data=[i[1] * 1e-9 for i in density_table])
build_chart(title=f'S(F0), H={H} km', xlabel='F0', ylabel='S', x_data=F0_list, y_data=S_list)
build_chart(title=f'T(F0), H={H} km', xlabel='F0', ylabel='T', x_data=F0_list, y_data=T_list)
build_chart(title=f'W(F0), H={H} km', xlabel='F0', ylabel='W', x_data=F0_list, y_data=W_list)
# =========================================================================================================================
