from data import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt

theta_list = list(np.arange(0, 2 * math.pi + d_theta, d_theta))
r_list = []
p_list = []
OMEGA_list = []
i_list = []
omega_list = []
e_list = []
tau_list = []

a = get_a(ra=Earth_radius + h_a, rp=Earth_radius + h_p)
e = get_e(ra=Earth_radius + h_a, rp=Earth_radius + h_p, a=a)
p = get_p(a=a, e=e)
omega = 0
tau = 0
r = get_r(p=p, e=e, theta=theta_list[0])


p_list.append(p)
OMEGA_list.append(OMEGA)
omega_list.append(omega)
i_list.append(i)
e_list.append(e)
tau_list.append(tau)


def iterative_loop():
    global r, p, OMEGA, omega, i, e, tau
    r1 = p1 = OMEGA1 = omega1 = i1 = e1 = tau1 = 0

    for theta in theta_list:
        print(theta)
        # Компоненты возмущающих ускорений
        # ===============================
        T = T1(r=r, i=i, u=theta + omega)
        S = S1(r=r, i=i, u=theta + omega)
        W = W1(r=r, i=i, u=theta + omega)
        # T = S = W = 0
        # ===============================

        # Радиус
        # ==============================
        r = get_r(p=p, e=e, theta=theta)
        r_list.append(r)
        # ==============================

        F = geT_F(r=r, S=S, T=T, theta=theta, e=e, p=p)

        # Новые элементы
        # ======================================================================================================
        p1 = R_p(r=r, T=T, F=F) + p * d_theta
        OMEGA1 = R_OMEGA(W=W, F=F, r=r, p=p, u=theta + omega, i=i) + OMEGA * d_theta
        i1 = R_i(W=W, F=F, r=r, p=p, u=theta + omega) + i * d_theta
        omega1 = R_omega(F=F, S=S, theta=theta, e=e, T=T, r=r, p=p, W=W, i=i, u=theta + omega) + omega * d_theta
        e1 = R_e(F=F, S=S, theta=theta, T=T, r=r, p=p, e=e) + e * d_theta
        tau1 = R_tau(F=F, p=p) + tau * d_theta
        # ======================================================================================================

        # Занесение новых данных в контейнеры
        # ===================================
        p_list.append(p1)
        OMEGA_list.append(OMEGA1)
        i_list.append(i1)
        omega_list.append(omega1)
        e_list.append(e1)
        tau_list.append(tau1)
        # ===================================

        p, i, e, tau, OMEGA, omega = p1, i1, e1, tau1, OMEGA1, omega1


def chart(x, y, title='', xlabel='', ylabel=''):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()


def main():
    iterative_loop()

    x = [r_list[i] * math.cos(theta_list[i]) for i in range(len(theta_list[:10]))]
    y = [r_list[i] * math.sin(theta_list[i]) for i in range(len(theta_list[:10]))]
    chart(x=x, y=y)


if __name__ == '__main__':
    main()
