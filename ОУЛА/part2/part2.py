from func import *
import matplotlib.pyplot as plt
import numpy as np
import math


def find_Psi_and_X(x1, x2, psi1, psi2, tk, dt):
    _x1 = x1
    _x2 = x2
    _psi1 = psi1
    _psi2 = psi2
    t = 0

    while t <= tk:
        x1 = _x1 + R_x1(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        x2 = _x2 + R_x2(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        psi1 = _psi1 + R_psi1(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        psi2 = _psi2 + R_psi2(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        _x1 = x1
        _x2 = x2
        _psi1 = psi1
        _psi2 = psi2

        t += dt
    return (x1, x2, psi1, psi2)


func = lambda psi1, psi2: criterion_function(*find_Psi_and_X(x1=1, x2=1, psi1=psi1, psi2=psi2, tk=4, dt=.01))
step = .001
rate = 1e-8
psi1 = 0
psi2 = 0
f1 = f2 = func(psi1, psi2)


def rotate_vector(x, y, angle):
    x1 = x * math.cos(angle) - y * math.sin(angle)
    y1 = y * math.cos(angle) + x * math.sin(angle)
    return x1, y1


# while 1:
#     for angle in np.linspace(0, 2 * math.pi, 100):
#         x, y = rotate_vector(x=1, y=0, angle=angle)
#         if func(psi1 + x * step, psi2 + y * step) < func(psi1, psi2):
#             psi1 += x * step
#             psi2 += y * step
#             print(func(psi1, psi2), 'psi1', psi1, 'psi2', psi2, 'vector: ', [x,y])
#             # break
#             # input()
i = 0
while 1:
    f_min = func(psi1, psi2)
    direct = (1, 0)
    # Минимальное направление
    # ================================================================
    for angle in np.linspace(0, 2 * math.pi, 100):
        x, y = rotate_vector(x=1, y=0, angle=angle)
        # if func(psi1 + x * step, psi2 + y * step) < func(psi1, psi2):
        #     direct = (x, y)

        if func(psi1 + x * step, psi2 + y * step) < f_min:
            direct = (x, y)
            f_min = func(psi1 + x * step, psi2 + y * step)
            # print(direct)
    # ================================================================

    x, y = direct

    # _step = -10
    # final_step = 0
    # delta = 0
    # while _step < 10:
    #     # print((func(psi1 + _step * x, psi2 + _step * y) - func(psi1, psi2)))
    #     if (func(psi1 + _step * x, psi2 + _step * y) - func(psi1, psi2)) < delta:
    #         # print('+++++++++++')
    #         delta = func(psi1 + _step * direct[0], psi2 + _step * direct[1]) - func(psi1, psi2)
    #         final_step = _step
    #     _step += 1e-2
    # print('[STEP LOG]', final_step)

    final_step = step
    if func(psi1 + x * step, psi2 + y * step) > func(psi1, psi2):
        break
    psi1 += x * step
    psi2 += y * step
    if i % 100 == 0:
        print(func(psi1, psi2), 'psi1', psi1, 'psi2', psi2, 'vector: ', [x, y])
    i += 1

    # input()

# print(func(psi1, psi2), 'psi1', psi1, 'psi2', psi2, 'vector: ', [x, y])
print(func(psi1, psi2), 'psi1', psi1, 'psi2', psi2)


def build(x1, x2, psi1, psi2, tk, dt):
    _x1 = x1
    _x2 = x2
    _psi1 = psi1
    _psi2 = psi2
    t = 0
    t_list = []
    x1_list = []
    x2_list = []
    psi1_list = []
    psi2_list = []

    while t <= tk:
        t_list.append(t)
        x1_list.append(x1)
        x2_list.append(x2)
        psi1_list.append(psi1)
        psi2_list.append(psi2)

        x1 = _x1 + R_x1(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        x2 = _x2 + R_x2(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        psi1 = _psi1 + R_psi1(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        psi2 = _psi2 + R_psi2(x1=_x1, x2=_x2, psi1=_psi1, psi2=_psi2) * dt
        _x1 = x1
        _x2 = x2
        _psi1 = psi1
        _psi2 = psi2

        t += dt

    plt.plot(t_list, x1_list, label='x1')
    plt.plot(t_list, x2_list, label='x2')
    plt.plot(t_list, [-1 / 6 * i for i in psi2_list], label='u')
    plt.title(f'Значение критерия {round(criterion_function(x1, x2, psi1, psi2), 8)}')
    plt.legend()
    plt.grid()
    plt.savefig('chart.png')
    plt.show()


# build(x1=1, x2=1, psi1=19.11822019, psi2=33.35435676, tk=4, dt=.01)
build(x1=1, x2=1, psi1=psi1, psi2=psi2, tk=4, dt=.01)

x = []
y = []
z = []
s = [10] * 40

# for i in np.arange(-40, 40):
#     for j in np.arange(-40, 40):
#         x.append(i)
#         y.append(j)
#         z.append(func(i, j))
#
# print(func(psi1=0, psi2=0))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x, y, z, s=10)
# ax.scatter([19.11822019], [33.35435676], [func(psi1=19.11822019, psi2=33.35435676)], s=40)
# ax.scatter([0], [0], [func(psi1=0, psi2=0)], s=40)
# ax.scatter([0 + step], [0], [func(psi1=0 + step, psi2=0)], s=40)
# ax.scatter([0], [0 + step], [func(psi1=0, psi2=0 + step)], s=40)
# plt.show()
