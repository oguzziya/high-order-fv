import numpy as np

class Step:
    def __call__(self, x):
        q = np.zeros([len(x)+2])
        q[1:-1][x < 0.5] = 1.
        q[1:-1][x < 0.3] = -0.2
        return q

class Sin:
    def __call__(self, x):
        q = np.zeros([len(x) + 2])
        q[1:-1] = 0.5*np.sin(10*x) + 0.5
        return q