from math import radians

# ИСХОДНЫЕ ДАННЫЕ
# -----------------------------------------
apocenter_height = 350                 # Hа
pericenter_height = 240                # Hп
mood = radians(10)                     # i
ascending_node_longitude = radians(5)  # 𝛀
pericenter_argument = radians(0)       # ω
mean_anomaly = radians(60)             # M
# -----------------------------------------

# КОНСТАНТЫ
# -------------------
μ = 398603
R = 6371
SIGMA_X = 1e-3
a = 6378136 / 1e3
ez_sqr = 0.0067385254
# -------------------
