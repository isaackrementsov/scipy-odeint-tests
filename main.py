import Reaction
import Gravity
import Virus
import CircuitLRC
import numpy as np

# Model an RLC circuit with 40hz AC voltage
t = np.linspace(0, 1, 1000)

Q0 = 0
I0 = 0.01

R = 2
L = 1
C = 0.00015

w = 2*np.pi*40
phi = 0
def E(t):
	return np.cos(3*t)

lrc = CircuitLRC.CircuitLRC(Q0, I0, R, C, L, E, t)
lrc.graph('circuit', 'Time (s)', 'Current (A)')

# Kinetic model of an chemical reaction
#t = np.linspace(0, 3, 100)
#Z0 = [1, 1, 0, 0]
#reaction = Reaction.Reaction(Z0, t)
#reaction.graph('concentrations', 'Time (s)', 'Concentration (M)')

# Motion under a gravitational field
#t = np.linspace(0, 50)
#initial_r_v = [1, 10]
#reaction = Gravity.Gravity(initial_r_v, t)
#reaction.graph('gravity', 'Time (s)', 'Position (m)')

# (Simple) virus spread model
#t = np.linspace(0, 50)
#I0 = 0.01
#P = 1
#ki = 2
#kc = 0.2
#virus = Virus.Virus(I0, P, ki, kc, t)
#virus.graph('virus', 'Time', 'Infected')