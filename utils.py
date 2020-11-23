import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Helvetica"

def plot_animated(ax, x, q_list, dx, colors, legends, animate=True):

    i = 0
    for q in q_list:
        ax.step(x, q[1:-1], color=colors[i], label=legends[i])
        ax.plot(x - dx / 2, q[1:-1], 'o', markersize=3, color=colors[i])
        i += 1

    ax.plot(x, np.ones_like(x), linestyle=":", color="gray")
    ax.plot(x, np.zeros_like(x), linestyle=":", color="gray")
    ax.set_xticks(x)
    ax.set_ylim([-0.3, 1.3])
    ax.set_xticklabels([])
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc="lower left")

    if animate:
        plt.draw()
        plt.pause(0.0001)
        ax.clear()
        #plt.close(fig)
    else:
        plt.show()