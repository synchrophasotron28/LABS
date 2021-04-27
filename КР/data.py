import math

# 11 ВАРИАНТ
# ИСХОДНЫЕ ДАННЫЕ
# ======================
i = math.radians(20.8)
# h_a = 1740
# h_p = 350

# Новые данные для моделирования возмущения от луны
h_a = 170_000
h_p = 130_000

# h_a = h_p = 1400
OMEGA = math.radians(10)
U = math.radians(7)
Sa = 23
m = 1700
C_xa = 3.5
Fa = 125
# ======================

d_theta = 1e-2
Earth_radius = 6371
Earth_gravity_potential = 698603 * 3600 * 3600
