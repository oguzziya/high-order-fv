import numpy as np

class AdvectionFlux:
    def __init__(self, advection_velocity):
        self.a = advection_velocity
    def __call__(self, q):
        return self.a * q
    def velocity(self, q):
        return self.a

class BurgersFlux:
    def __call__(self, q):
        return 0.5 * np.square(q)
    def velocity(self, q):
        return 0.5*(q[:-2] + q[2:])

class LaxWendroff:
    def __init__(self, dx, dt, flux):
        self.dx = dx
        self.dt = dt
        self.flux = flux

    def __call__(self, q):
        q[1:-1] = q[1:-1] - self.dt/self.dx * (self.numerical_flux(q, 1) - self.numerical_flux(q, 0))
        return q, self.dt

    def numerical_flux(self, q, i):
        return 0.5*(self.flux(q[i:-2+i]) + self.flux(q[i+1:len(q)-1+i])) - 0.5*self.dt/self.dx*(self.flux(q[i+1:len(q)-1+i]) - self.flux(q[i:-2+i]))*np.square(self.flux.velocity(q))


class Godunov:
    def __init__(self, dx, dt, flux, courant=None, limiter=None):
        self.dx = dx
        self.dt = dt
        self.co = courant
        self.flux = flux
        self.limiter = limiter
        self.dx = dx

    def __call__(self, q):
        # Adaptive time stepping or constant time stepping
        if self.co is not None:
            dt = self.co * self.dx / np.max(q)
        else:
            dt = self.dt

        v = dt/self.dx

        # Flux differencing formula
        q[1:-1] = q[1:-1] - v * (self.numerical_flux(q[1:-1]) - self.numerical_flux(q[:-2]))

        # Apply limiter
        if self.limiter is not None:
            with np.errstate(divide='ignore', invalid='ignore'):
                # Left jump variable
                theta_l = (q[:-2] - np.hstack([q[-2], q[:-3]])) / (q[1:-1] - q[:-2])
                # Right jump variab-
                theta_r = (q[1:-1] - q[:-2]) / (q[2:] - q[1:-1])

            # Check division by zeros
            theta_l[np.isnan(theta_l)] = 0.0
            theta_r[np.isnan(theta_r)] = 0.0

            # Apply limiter
            lim_l = self.limiter(theta_l) * 10
            lim_r = self.limiter(theta_r) * 10

            q[1:-1] -= 0.5*v*(self.dx - self.flux.velocity(q)*dt)*(lim_r*(q[2:] - q[1:-1]) - lim_l*(q[1:-1] - q[:-2]))

            q[q > 1.] = 1.

        return q, dt

    def numerical_flux(self, q):
        return self.flux(q)