import math

# Формулы для рассчёта компонентов возмущающего ускорения,
# вызванного нецентральность гравитационного поля Земли
# ===================================================================================
Epsilon = 398603 * 66.07 * 1e3
S1 = lambda r, i, u: Epsilon / r ** 4 * (3 * math.sin(i) ** 2 * math.sin(u) ** 2 - 1)
T1 = lambda r, i, u: -Epsilon / r ** 4 * math.sin(i) ** 2 * math.sin(2 * u)
W1 = lambda r, i, u: -Epsilon / r ** 4 * math.sin(2 * i) * math.sin(u)
# ===================================================================================

# Правые части диф уравнений метода оскулирующих элементов
# =====================================================================================================================
_p = lambda r, T, F: 2 * r * T * F
_OMEGA = lambda W, F, r, p, u, i: W * F * r / p * math.sin(u) / math.sin(i)
_i = lambda W, F, r, p, u: W * F * r / p * math.cos(u)
_omega = lambda F, S, theta, e, T, r, p, W, i, u: F * (
        -S * math.cos(theta) / e + T * (1 + r / p) * math.sin(theta) / e - W * r / p(1 / math.tan(i)) * math.sin(u))
_e = lambda F, S, theta, T, r, p, e: F * (S * math.sin(theta) + T * ((1 + r / p) * math.cos(theta) + e * r / p))
_tau = lambda F, p: F * math.sqrt(398603 / p)

F = lambda r, S, T, theta, e: (398603 / r ** 2 + S * math.cos(theta) / e - T * (1 + r / p) * math.sin(theta) / e) ** -1
# =====================================================================================================================

# Вспомогательные функции
# ========================================================
get_a = lambda ra, rp: 0.5 * (ra + rp)
get_e = lambda ra, rp, a: (ra - rp) / (2 * a)
get_r = lambda p, e, theta: p / (1 + e * math.cos(theta))
get_p = lambda a, e: a * (1 - e ** 2)
# ========================================================
