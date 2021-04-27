from data import *
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import moon

sigma_x = get_sigma_x(Cxa=C_xa, Sa=Sa, m=m)

revolutions = 2 * 4.5  # Количество оборотов
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

spacecraft_X, spacecraft_Y, spacecraft_Z = [], [], []
moon_X, moon_Y, moon_Z = [], [], []


def iterative_loop():
    global r, p, OMEGA, omega, i, e, tau
    global spacecraft_X, spacecraft_Y, spacecraft_Z
    global moon_X, moon_Y, moon_Z

    r1 = p1 = OMEGA1 = omega1 = i1 = e1 = tau1 = 0

    for theta in theta_list:
        if theta_list.index(theta) % 1000 == 0:
            print(theta)

        # time = get_t_from_tau(tau=tau, theta=theta, p=p, e=e)
        # print('[LOG]', theta, time / 3600)
        # Радиус
        # ==============================
        r = get_r(p=p, e=e, theta=theta)
        r_list.append(r)
        # ==============================

        # H = find_H(Ra=r, theta=theta, i=i, big_omega=OMEGA, omega=omega, p=p, e=e, tau=tau)  # высота
        # density = find_density(H=H)  # плотность
        #
        # H_list.append(H)
        # Density_list.append(density)

        # Скорости
        # ================================
        # Vr = get_Vr(p=p, theta=theta, e=e)
        # Vt = get_Vt(p=p, theta=theta, e=e)
        # V = math.hypot(Vr, Vt)
        # ================================

        # Компоненты возмущающих ускорений
        # ===============================
        # T = T1(r=r, i=i, u=theta + omega)
        # S = S1(r=r, i=i, u=theta + omega)
        # W = W1(r=r, i=i, u=theta + omega)
        # # T = S = W = 0
        #
        # S = S2(sigma_x=sigma_x, density=density, V=V, Vr=Vr) * 1e3
        # T = T2(sigma_x=sigma_x, density=density, V=V, Vt=Vt) * 1e3
        # W = W2

        # Возмущения от Луны
        # =================================================================================================
        current_time = get_t_from_tau(tau=tau, theta=theta, p=p, e=e)
        moon_coord = moon.find_moon_position(t=current_time)
        spacecraft_coord = get_agesk(theta=theta, ra=r, i=i, big_omega=OMEGA, omega=omega)

        moon_X.append(moon_coord[0])
        moon_Y.append(moon_coord[1])
        moon_Z.append(moon_coord[2])

        spacecraft_X.append(spacecraft_coord[0])
        spacecraft_Y.append(spacecraft_coord[1])
        spacecraft_Z.append(spacecraft_coord[2])

        S, T, W = moon.find_moon_STW(moon_coord=moon_coord, spacecraft_coord=spacecraft_coord, theta=theta)
        # =================================================================================================

        # S = T = W = 0
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
        #
        # p1 = p + runge_p(r=r, S=S, T=T, e=e, p=p, theta=theta, d_theta=d_theta)
        # OMEGA1 = OMEGA + runge_OMEGA(S=S, T=T, W=W, r=r, e=e, p=p, omega=omega, i=i, theta=theta, d_theta=d_theta)
        # i1 = i + runge_i(S=S, T=T, W=W, r=r, e=e, p=p, omega=omega, theta=theta, d_theta=d_theta)
        # omega1 = omega + runge_omega(S=S, T=T, W=W, r=r, e=e, p=p, omega=omega, theta=theta, d_theta=d_theta)
        # e1 = e + runge_e(S=S, theta=theta, T=T, r=r, p=e, e=e, d_theta=d_theta)
        # tau1 = tau + runge_tau(r=r, S=S, T=T, e=e, p=p, theta=theta, d_theta=d_theta)

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
    # plt.plot(len(y) * [math.pi], y, 'r')
    # plt.plot(len(y) * [2 * math.pi], y, 'r')
    # plt.plot(len(y) * [3 * math.pi], y, 'r')
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


def chart_3d():
    global spacecraft_X, spacecraft_Y, spacecraft_Z
    global moon_X, moon_Y, moon_Z

    s = [1] * len(moon_X)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Луна
    # ================================================================
    ax.scatter(moon_X, moon_Y, moon_Z, s, color='dimgray', label='Траектория Луны')
    # ax.scatter(moon_X[0], moon_Y[0], moon_Z[0], s=moon.moon_radius, color='darkgray')
    ax.scatter(moon_X[-1], moon_Y[-1], moon_Z[-1], s=moon.moon_radius, color='silver')
    # ================================================================

    n = 30
    X = [i for i in spacecraft_X if (spacecraft_X.index(i) + 1) % n == 0]
    Y = [i for i in spacecraft_Y if (spacecraft_Y.index(i) + 1) % n == 0]
    Z = [i for i in spacecraft_Z if (spacecraft_Z.index(i) + 1) % n == 0]
    s = [1] * len(X)

    # КЛА
    # ================================================================
    # ax.scatter(spacecraft_X, spacecraft_Y, spacecraft_Z, s, color='darkkhaki', label='Траектория КЛА')
    ax.scatter(X, Y, Z, s, color='darkkhaki', label='Траектория КЛА')
    ax.scatter(spacecraft_X[0], spacecraft_Y[0], spacecraft_Z[0], s=80, color='orange', label='Начальное положение КЛА')
    ax.scatter(spacecraft_X[-1], spacecraft_Y[-1], spacecraft_Z[-1], s=80, color='red', label='Конечное положение КЛА')
    # ================================================================

    # Земля
    # ======================================================
    ax.scatter([0], [0], [0], s=Earth_radius, color='green')
    # ======================================================

    plt.title('Траектории движения Луны и КЛА');

    ax.legend()
    plt.savefig('./charts/{}.png'.format('traektoria'))
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

    chart_3d()


if __name__ == '__main__':
    main()
