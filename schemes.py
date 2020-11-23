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
        return q

class LaxWendroff:
    def __init__(self, dx, dt, flux):
        self.dx = dx
        self.dt = dt
        self.flux = flux

    def step(self, q):
        q[1:-1] = q[1:-1] - self.dt/self.dx * (self.numerical_flux(q, 1) - self.numerical_flux(q, 0))
        return q

    def numerical_flux(self, q, i):
        return 0.5*(self.flux(q[i:-2+i]) + self.flux(q[i+1:len(q)-1+i])) - 0.5*self.dt/self.dx*(self.flux(q[i+1:len(q)-1+i]) - self.flux(q[i:-2+i]))*np.square(self.flux.velocity(q[1:-1]))


class Upwind:
    def __init__(self, dx, dt, flux, limiter=None):
        self.dx = dx
        self.dt = dt
        self.flux = flux
        self.limiter = limiter
        self.dx = dx

    def step(self, q):
        q[1:-1] = q[1:-1] - self.dt/self.dx * (self.numerical_flux(q, 1) - self.numerical_flux(q, 0))
        if self.limiter is not None:
            q[1:-1] -= 0.5*self.dt/self.dx*(self.dx - q[1:-1]*self.dt)*self.limiter.slope(q, self.dx)
        return q

    def numerical_flux(self, q, i):
        return self.flux(q[i:-2+i])