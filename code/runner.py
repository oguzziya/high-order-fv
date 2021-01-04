import numpy as np
from initial_conditions import *
from utils import *
from schemes import *
from limiters import *

# Space discretization
x_0 = 0.0
x_1 = 1.0
nx = 50
dx = (x_1 - x_0) / nx
x = np.linspace(x_0 + 0.5*dx, x_1 - 0.5*dx, nx)

# Time discretization
num_steps = 1
dt = 0.01

init = Step()
flux = AdvectionFlux(0.6)

initial_data = init(x)

print(dt*0.6/dx)

methods = [ [init(x), Godunov(dx, dt, flux=flux, limiter=Upwind()), 'Upwind', 'black', '-'],
            [init(x), Godunov(dx, dt, flux=flux, limiter=vanLeer()), 'van Leer', 'blue', '--'],
            [init(x), Godunov(dx, dt, flux=flux, limiter=MC()), 'MC', 'green', '-.'],
            [init(x), Godunov(dx, dt, flux=flux, limiter=SuperBee()), 'SuperBee', 'red', ':'],
            #[init(x), LaxWendroff(dx, dt, flux=flux), 'Lax-Wendroff', 'black', '--'],
          ]
t = 0.0

for i in range(num_steps):
    plot_list = []
    legend_list = []
    color_list = []
    style_list = []
    for q, update_method, legend, color, style in methods:
        q[0] = q[-2]
        q[-1] = q[1]
        q, dt = update_method(q)
        plot_list.append(q)
        legend_list.append(legend)
        color_list.append(color)
        style_list.append(style)
    t += dt

    #plot_animated(ax, x, plot_list, dx, t, color_list, style_list, legend_list, type='CONTINIOUS', animate=True)
    #if i == num_steps-1:
    #    plot_animated(ax, x, plot_list, dx, t, color_list, style_list, legend_list, type='CONTINIOUS', animate=False)

plot_animated(ax, x, plot_list, dx, t, color_list, style_list, legend_list, type='CONTINIOUS', animate=False, save=True, file_name=("limiter"+"{:.3f}".format(t)))