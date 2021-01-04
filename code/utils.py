import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
plt.rcParams["font.family"] = "Helvetica"

plt.rc('text', usetex=True)
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
fig = plt.figure(figsize=(4,3))
ax = fig.add_subplot(1, 1, 1)

def plot_animated(ax, x, q_list, dx, t, colors, style, legends, animate=True, type='FV', save=False, file_name=None):

    i = 0
    for q in q_list:
        if type == 'FV':
            ax.step(x+dx/2, q[1:-1], color=colors[i], label=legends[i])
            ax.plot(x, q[1:-1], 'o', markersize=3, color=colors[i])
            i += 1
        elif type == 'CONTINIOUS':
            ax.plot(x, q[1:-1], color=colors[i], label=legends[i], linestyle=style[i])
            ax.plot(x, q[1:-1], 'o', markersize=3, color=colors[i], linestyle=style[i])
            i += 1

    ax.plot(x, np.ones_like(x), linestyle=":", color="gray")
    ax.plot(x, np.zeros_like(x), linestyle=":", color="gray")
    ax.set_xlabel("x")
    ax.set_ylabel("q")
    ax.set_title("Time: " + "{:.3f}".format(t) + " s")
    ax.set_xticks(x)
    ax.set_ylim([0.8, 1.2])
    ax.set_xlim([0.2, 0.7])
    ax.set_xticklabels([])
    #ax.grid()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc="upper left")

    if animate:
        plt.draw()
        plt.pause(0.0001)
        ax.clear()
    else:
        if save:
            mlp.use('pgf')
            plt.rcParams.update({
                "pgf.rcfonts": False,
            })
            fig.savefig(file_name + ".pdf")
            fig.savefig(file_name + ".pgf")
        else:
            plt.show()