from data import *
from functions import *
import numpy as np

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


def iterative_loop():
    for theta in theta_list:
        print(theta)


def chart(x, y, title, xlabel, ylabel):
    pass


def main():
    iterative_loop()


if __name__ == '__main__':
    main()
