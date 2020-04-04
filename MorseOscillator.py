import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class MorseOscillator:

    def __init__(self, initial_radius, initial_velocity, well_depth, well_width, equilibrium_distance, mass, t_interval):
        self.t = t_interval
        self.initial_values = [initial_radius, initial_velocity]
        self.De = well_depth
        self.a = well_width
        self.re = equilibrium_distance
        self.m = mass

    def oscillator(self, vars, t):
        r = vars[0]
        v = vars[1]

        De = self.De
        a = self.a
        re = self.re
        m = self.m

        expn = np.exp(-a*(r - re))

        drdt = v
        dvdt = 2*De*a*expn*(expn - 1)/m

        return [drdt, dvdt]

    def solve(self):
        Motion = odeint(self.oscillator, self.initial_values, self.t)

        return Motion

    def graph(self, image_name, x_label, y_label):
        Motion = self.solve()

        r = Motion[:,1]

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111)

        ax.plot(self.t, r)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        fig.savefig(image_name + '.png')
