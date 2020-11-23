import numpy as np

class DownwindSlope:

    def slope(self, q, dx):
        slope = (q[2:] - 2*q[1:-1] + q[:-2])/dx
        return slope

class UpwindSlope:

    def slope(self, q, dx):
        slope = (q[1:-1] - 2 * q[:-2] + np.hstack([q[0], q[:-3]]))/dx
        return slope

class CentralSlope:

    def slope(self, q, dx):
        slope = (q[2:] - q[:-2] - q[1:-1] + np.hstack([q[0], q[:-3]]))/(2.0*dx)
        return slope

class MinMod:

    def slope(self, q, dx):
        slope_d = (q[2:] - 2 * q[1:-1] + q[:-2]) / dx
        slope_u = (q[1:-1] - 2 * q[:-2] + np.hstack([q[0], q[:-3]])) / dx
        value = np.max(np.vstack([np.zeros_like(slope_u), np.min(np.vstack([slope_d, slope_u]), axis=0)]), axis=0)
        return value
