import numpy as np

class Upwind:

    def __call__(self, theta):
        return 0.0

class LaxWendroffLOL:

    def __call__(self, theta):
        return 1.0

class BeamWarming:

    def __call__(self, theta):
        return theta

class Fromm:

    def __call__(self, theta):
        return 0.5*(1.0 + theta)

class MinMod:

    def __call__(self, theta):
        first_cond = np.min(np.vstack([theta, np.ones_like(theta)]), axis=0)

        return np.max(np.vstack([np.zeros_like(theta), first_cond]), axis=0)

class SuperBee:

    def __call__(self, theta):
        first_cond =  np.min(np.vstack([2.0*theta, np.ones_like(theta)]), axis=0)
        second_cond = np.min(np.vstack([theta, 2.0*np.ones_like(theta)]), axis=0)

        return np.max(np.vstack([np.zeros_like(theta), first_cond, second_cond]), axis=0)

class MC:

    def __call__(self, theta):

        first_cond =  np.min(np.vstack([0.5*theta + 0.5, 2.0*np.ones_like(theta), 2.0*theta]), axis=0)

        return np.max(np.vstack([np.zeros_like(theta), first_cond]), axis=0)


class vanLeer:

    def __call__(self, theta):
        with np.errstate(divide='ignore', invalid='ignore'):
            lim = (theta + np.abs(theta))/(1.0 +  np.abs(theta))

        lim[np.isnan(lim)] = 0.0
        return lim

