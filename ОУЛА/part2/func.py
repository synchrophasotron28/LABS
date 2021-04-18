# Правые части систем уравнений для численного интергрирования
R_x1 = lambda x1, x2, psi1, psi2: 3*x2
R_x2 = lambda x1, x2, psi1, psi2: x1 - 1 / 6 * psi2
R_psi1 = lambda x1, x2, psi1, psi2: -psi2
R_psi2 = lambda x1, x2, psi1, psi2: -4 * x2 - 3 * psi1

# Функция критерий
criterion_function = lambda x1, x2, psi1, psi2: (psi1 - 2 * x1) ** 2 + (psi2 - 4 * x2) ** 2
