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
omega = -1 #????
tau = -1 #????

def iterative_loop():
    for theta in theta_list:
        print(theta)


def main():
    iterative_loop()


if __name__ == '__main__':
    main()
