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
    plt.plot(t_list, [-1 / (2 * 3) * i for i in psi2_list], label='u')
    for i in range(len(t_list)):
        print(f'{t_list[i]} {x1_list[i]} {x2_list[i]} {-1 / (2 * 3) * psi2_list[i]}')
    plt.title(f'Значение критерия {round(criterion_function(x1, x2, psi1, psi2), 8)}')
    plt.legend()
    plt.grid()
    plt.savefig('chart.png')
    plt.show()


# build(x1=1, x2=1, psi1=19.00015663252696, psi2=33.1922603980915, tk=4, dt=.01)
# build(x1=1, x2=1, psi1=19.059020751361658, psi2=33.273064692004475, tk=4, dt=.01)
#
# build(x1=1, x2=1, psi1=19.116094203710134, psi2=33.351463687549064, tk=4, dt=.01)
# build(x1=1, x2=1, psi1=19.11822019, psi2=33.35435676, tk=4, dt=.01)
build(x1=1, x2=1, psi1=psi1, psi2=psi2, tk=4, dt=.01)

# build(x1=1, x2=1, psi1=31.73750843904442, psi2=55.21301214267813, tk=4, dt=.01) # Это для W
# build(x1=1, x2=1, psi1=19.285303256172018, psi2=33.88677171925858, tk=4, dt=.01) # Это для Q
# build(x1=1, x2=1, psi1=19.11543277037631, psi2=33.35058625164072, tk=4, dt=.01) # Это для лямбд

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

'''
Обычное
t0=0 x1=1                   x2=1                    u=-5.55905946
t1=1 x1=1.0111201654177928  x2=-0.3026780794602267  u=-0.9450667740473899
tk=4 x1=0.03617205046121464 x2=-0.00169383826522897 u=0.00019678833503765353


С увеличением W
t0=0    x1=1                    x2=1                        u=-5.5213012142678135
t1=1    x1=1.0120846990101422   x2=-0.3055726152603542      u=-0.9477719978847985
tk=4    x1=0.04732491834144866  x2=0.0063573937198358145    u=0.0007767286839485698


С увеличением q22
t0=0    x1=1                    x2=1                        u=-5.647795286543097
t1=1    x1=1.0125034872398249   x2=-0.2935259147229142      u=-0.9402484618961553
tk=4    x1=0.2650623429597535  x2=0.10898084394444502       u=-0.040090146324358006

С увеличением обеих лямбд
t0=0    x1=1                    x2=1                        u=-5.5584310419401195
t1=1    x1=1.0117212041711365   x2=-0.30230363077059397      u=-0.94525939288482
tk=4    x1=0.05706809709469048  x2=0.0008906972041678559    u=-0.03240742092597573

'''