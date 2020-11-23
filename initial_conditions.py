import numpy as np

def init_step(x):
    q = np.zeros([len(x)+2])
    q[1:-1][x < 0.4] = 1.
    q[1:-1][x < 0.2] = 0.
    return q

def init_sin(x):
    q = np.zeros([len(x) + 2])
    q[1:-1] = 0.5*np.sin(10*x) + 0.5
    return q