from func import *
import matplotlib.pyplot as plt


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
step = 0.1
rate = 0.1
psi1 = 20
psi2 = 20
# Минимизируем по psi1

d_psi1 = (func(psi1 + step, psi2) - func(psi1, psi2)) / step
d_psi2 = (func(psi1, psi2 + step) - func(psi1, psi2)) / step

from time import sleep

while 1:
    d_psi1 = (func(psi1 + step, psi2) - func(psi1, psi2)) / step
    d_psi2 = (func(psi1, psi2 + step) - func(psi1, psi2)) / step
    print(d_psi1, d_psi2)

    print('[BEFORE]',func(psi1, psi2))
    psi1 -= rate * d_psi1
    psi2 -= rate * d_psi2
    print(f'psi1: {psi1} psi2: {psi2}')
    print('[AFTER]',func(psi1, psi2))
    input()


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
    plt.legend()
    plt.grid()
    plt.show()
    print(x1, x2, psi1, psi2)


# [[19.11822019]
#  [33.35435676]]
build(x1=1, x2=1, psi1=19.11822019, psi2=33.35435676, tk=4, dt=.01)
print(criterion_function(x1=0.03612123531325777, x2=-0.001330149877266447, psi1=0.07251165346582268,
                         psi2=-0.003287971864588375))


print(func(0,0))
# import numpy as np
# x = np.linspace(-20, 20, 100)
# y = x
# z = [func(i,i) for i in x]
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(x, y, z, label='parametric curve')
# plt.show()