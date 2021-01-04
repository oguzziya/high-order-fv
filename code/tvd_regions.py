import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
from limiters import *


save = True
plt.rc('font', family="serif")
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(1, 1, 1)

x = np.linspace(0.0, 4.0, 800)

x1 = np.linspace(0.0, 0.5, 800)
x2 = np.linspace(0.5, 1.0, 800)
x3 = np.linspace(1.0, 2.0, 800)
x4 = np.linspace(2.0, 4.0, 800)

ax.fill_between(x1, x1, 2*x1, color="silver")
ax.fill_between(x2, x2, 1., color="silver")
ax.fill_between(x3, x3, 1., color="silver")
ax.fill_between(x4, 2., 1., color="silver")

file_name = "MC"
limiter = MC()
ax.plot(x, limiter(x), color="black")
ax.set_title(file_name)
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\phi$')

if save:
    mlp.use('pgf')
    plt.rcParams.update({
        "pgf.rcfonts": False,
    })
    fig.savefig(file_name + ".pdf")
    fig.savefig(file_name + ".pgf")
else:
    plt.show()