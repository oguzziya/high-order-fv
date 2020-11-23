import numpy as np
from initial_conditions import *
from utils import *
from schemes import *
from limiters import *

# Space discretization
x_0 = 0.0
x_1 = 1.0
nx = 100
dx = (x_1 - x_0) / nx
x = np.linspace(x_0 + 0.5*dx, x_1 - 0.5*dx, nx)

# Advection velocity
u = 1.0

# Time discretization
num_steps = 100
courant = 1.0
dt = dx * courant / u

methods = [ [init_sin(x), LaxWendroff(dx, dt, flux=BurgersFlux()), 'Lax-Wendroff', 'black'],
            [init_sin(x), Upwind(dx, dt, flux=BurgersFlux()), 'Upwind', 'red'],
            [init_sin(x), Upwind(dx, dt, flux=BurgersFlux(), limiter=MinMod()), 'Upwind Stabilized', 'blue']
          ]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#plot_animated(x, [q_plain, q_central, q_downwind, q_laxwendroff], dx, colors, legends, False)
for i in range(num_steps):
    plot_list = []
    legend_list = []
    color_list = []
    for q, method, legend, color in methods:
        q[0] = q[-2]
        q[-1] = q[1]
        q = method.step(q)
        plot_list.append(q)
        legend_list.append(legend)
        color_list.append(color)

    plot_animated(ax, x, plot_list, dx, color_list, legend_list, True)
plt.show()