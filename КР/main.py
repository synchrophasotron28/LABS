from data import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt

sigma_x = get_sigma_x(Cxa=C_xa, Sa=Sa, m=m)

revolutions = 8  # Количество оборотов
theta_list = list(np.arange(0, revolutions * math.pi + d_theta, d_theta))
r_list = []
p_list = []
OMEGA_list = []
i_list = []
omega_list = []
e_list = []
tau_list = []
S_list = []
T_list = []
W_list = []

# НАЧАЛЬНЫЕ ЗНАЧЕНИЯ
# ==========================================================
a = get_a(ra=Earth_radius + h_a, rp=Earth_radius + h_p)
e = get_e(ra=Earth_radius + h_a, rp=Earth_radius + h_p, a=a)
p = get_p(a=a, e=e)
omega = 0
tau = 0
r = get_r(p=p, e=e, theta=theta_list[0])
# ==========================================================


p_list.append(p)
OMEGA_list.append(OMEGA)
omega_list.append(omega)
i_list.append(i)
e_list.append(e)
tau_list.append(tau)

H_list = []
Density_list = []


def iterative_loop():
    global r, p, OMEGA, omega, i, e, tau
    r1 = p1 = OMEGA1 = omega1 = i1 = e1 = tau1 = 0

    for theta in theta_list:
        # Радиус
        # ==============================
        r = get_r(p=p, e=e, theta=theta)
        r_list.append(r)
        # ==============================

        H = find_H(Ra=r, theta=theta, i=i, big_omega=OMEGA, omega=omega, p=p, e=e, tau=tau)  # высота
        density = find_density(H=H)  # плотность

        H_list.append(H)
        Density_list.append(density)

        # Скорости
        # ================================
        Vr = get_Vr(p=p, theta=theta, e=e)
        Vt = get_Vt(p=p, theta=theta, e=e)
        V = math.hypot(Vr, Vt)
        # ================================

        # Компоненты возмущающих ускорений
        # ===============================
        T = T1(r=r, i=i, u=theta + omega)
        S = S1(r=r, i=i, u=theta + omega)
        W = W1(r=r, i=i, u=theta + omega)
        # T = S = W = 0

        S = S2(sigma_x=sigma_x, density=density, V=V, Vr=Vr)
        T = T2(sigma_x=sigma_x, density=density, V=V, Vt=Vt)
        W = 0
        # S2 = lambda sigma_x, density, V, Vr: -sigma_x * density * V * Vr
        # T2 = lambda sigma_x, density, V, Vt: -sigma_x * density * V * Vt
        # W2 = 0

        S_list.append(S)
        T_list.append(T)
        W_list.append(W)

        # ===============================

        F = geT_F(r=r, S=S, T=T, theta=theta, e=e, p=p)

        # Новые элементы
        # ======================================================================================================
        p1 = p + R_p(r=r, T=T, F=F) * d_theta
        OMEGA1 = OMEGA + R_OMEGA(W=W, F=F, r=r, p=p, u=theta + omega, i=i) * d_theta
        i1 = i + R_i(W=W, F=F, r=r, p=p, u=theta + omega) * d_theta
        omega1 = omega + R_omega(F=F, S=S, theta=theta, e=e, T=T, r=r, p=p, W=W, i=i, u=theta + omega) * d_theta
        e1 = e + R_e(F=F, S=S, theta=theta, T=T, r=r, p=p, e=e) * d_theta
        tau1 = tau + R_tau(F=F, p=p) * d_theta
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
    plt.plot(x, y, linewidth=1)
    if title == 'r(θ)':
        plt.plot(0, 0, marker='.', markersize=30, color='green', markerfacecolor='lightgreen')
        plt.plot(x[0], y[0], marker='.', markersize=20, color='blue', markerfacecolor='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    if title == 'ω(θ)':
        title = 'ω (θ)'
    plt.savefig('./charts/{}.png'.format(title))
    plt.show()


def main():
    iterative_loop()
    x = [r_list[i] * math.cos(theta_list[i]) for i in range(len(theta_list))]
    y = [r_list[i] * math.sin(theta_list[i]) for i in range(len(theta_list))]

    chart(x=x, y=y, title='r(θ)', xlabel='x, км', ylabel='y, км')
    chart(x=theta_list, y=e_list[:len(theta_list)], title='e(θ)', xlabel='θ, рад', ylabel='e')
    chart(x=theta_list, y=i_list[:len(theta_list)], title='i(θ)', xlabel='θ, рад', ylabel='i, рад')
    chart(x=theta_list, y=p_list[:len(theta_list)], title='p(θ)', xlabel='θ, рад', ylabel='p, км')
    chart(x=theta_list, y=OMEGA_list[:len(theta_list)], title='Ω(θ)', xlabel='θ, рад', ylabel='Ω, рад')
    chart(x=theta_list, y=omega_list[:len(theta_list)], title='ω(θ)', xlabel='θ, рад', ylabel='ω, рад')
    chart(x=theta_list, y=tau_list[:len(theta_list)], title='τ(θ)', xlabel='θ, рад', ylabel='τ, час')

    chart(x=theta_list, y=S_list[:len(theta_list)], title='S(θ)', xlabel='θ, рад', ylabel='S, км/ч^2')
    chart(x=theta_list, y=T_list[:len(theta_list)], title='T(θ)', xlabel='θ, рад', ylabel='T, км/ч^2')
    chart(x=theta_list, y=W_list[:len(theta_list)], title='W(θ)', xlabel='θ, рад', ylabel='W, км/ч^2')

    if H_list:
        chart(x=theta_list, y=H_list[:len(theta_list)], title='H(θ)', xlabel='θ, рад', ylabel='H, км')

    if Density_list:
        chart(x=theta_list, y=Density_list[:len(theta_list)], title='ρ(θ)', xlabel='θ, рад', ylabel='ρ, кг/м^3')


if __name__ == '__main__':
    main()
