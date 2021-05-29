import json
from flask import Flask
import math
from functions import *
from time import sleep
import threading

d_theta = 1e-2

DELAY_IN_SECS = .05

# h_a = 1740
# h_p = 350


h_a = 2500
h_p = 700


Earth_radius = 6371

a = get_a(ra=Earth_radius + h_a, rp=Earth_radius + h_p)
e = get_e(ra=Earth_radius + h_a, rp=Earth_radius + h_p, a=a)
p = get_p(a=a, e=e)
r = get_r(p=p, e=e, theta=0)
# print(r,p,e)
# r_list = []
# p_list = []
# OMEGA_list = []
# i_list = []
# omega_list = []
# e_list = []
# tau_list = []

flying_objects = {
    'object1':
        {
            'x': 0,
            'y': 0,
            'z': 0,
            'theta': 0,
            'h_a': 1740,
            'h_p': 350,
            'r': 6721.000000000001,
            'p': 7350.8671790722765,
            'OMEGA': math.radians(10),
            'omega': 0,
            'e': 0.09371628910463863,
            'U': math.radians(7),
            'tau': 0,
            'm': 1700,
            'i': math.radians(20.8)
        },

    'object2':
        {
            'x': 0,
            'y': 0,
            'z': 0,
            'theta': 0,
            'h_a': 2500,
            'h_p': 700,
            'r': 7071.0,
            'p': 7869.3816334211515,
            'OMEGA': math.radians(10),
            'omega': 0,
            'e': 0.11290929619872037,
            'U': math.radians(7),
            'tau': 0,
            'm': 1700,
            'i': math.radians(47)
        }

}


def loop():
    print('start')
    while True:
        for key in flying_objects.keys():
            r1 = p1 = OMEGA1 = omega1 = i1 = e1 = tau1 = 0

            r = flying_objects[key]['r']
            p = flying_objects[key]['p']
            OMEGA = flying_objects[key]['OMEGA']
            omega = flying_objects[key]['omega']
            i = flying_objects[key]['i']
            e = flying_objects[key]['e']
            tau = flying_objects[key]['tau']
            theta = flying_objects[key]['theta']

            S = T = W = 0
            F = geT_F(r=r, S=S, T=T, theta=theta, e=e, p=p)

            p1 = p + R_p(r=r, T=T, F=F) * d_theta
            OMEGA1 = OMEGA + R_OMEGA(W=W, F=F, r=r, p=p, u=theta + omega, i=i) * d_theta
            i1 = i + R_i(W=W, F=F, r=r, p=p, u=theta + omega) * d_theta
            omega1 = omega + R_omega(F=F, S=S, theta=theta, e=e, T=T, r=r, p=p, W=W, i=i, u=theta + omega) * d_theta
            e1 = e + R_e(F=F, S=S, theta=theta, T=T, r=r, p=p, e=e) * d_theta
            tau1 = tau + R_tau(F=F, p=p) * d_theta

            theta += d_theta
            r1 = get_r(p=p1, e=e1, theta=theta)

            x, y, z = get_agesk(theta=theta, ra=r1, i=i1, big_omega=OMEGA1, omega=omega1)
            flying_objects[key]['r'] = r1
            flying_objects[key]['p'] = p1
            flying_objects[key]['OMEGA'] = OMEGA1
            flying_objects[key]['omega'] = omega1
            flying_objects[key]['i'] = i1
            flying_objects[key]['e'] = e1
            flying_objects[key]['tau'] = tau1
            flying_objects[key]['theta'] = theta
            flying_objects[key]['x'] = x
            flying_objects[key]['y'] = y
            flying_objects[key]['z'] = z
        sleep(DELAY_IN_SECS)


loop_thread = threading.Thread(target=loop)

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps(flying_objects)


if __name__ == "__main__":
    loop_thread.start()
    app.run()
