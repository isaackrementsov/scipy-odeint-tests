import Reaction
import Gravity
import Virus
import CircuitLRC
import MorseOscillator
import numpy as np


# Morse potential oscillator
t = np.linspace(0, 20, 1000)

r0 = 0
v0 = 1

De = 5
re = 1
a = 0.6
m = 1

oscillator = MorseOscillator.MorseOscillator(r0, v0, De, a, re, m, t)
oscillator.graph('morse', 'Time', 'Radius')

# Model an RLC circuit with 40hz AC voltage
#t = np.linspace(0, 3, 1000)

#Q0 = 0
#I0 = 0

#R = 2
#L = 1
#C = 0.000015

#Emax = 5
#w = 2*np.pi*40
#phi = 0
#def E(t):
#	return Emax*np.cos(w*t + phi)

#lrc = CircuitLRC.CircuitLRC(Q0, I0, R, C, L, E, t)
#lrc.graph('circuit', 'Time (s)', 'Current (A)')


# Kinetic model of an chemical reaction
#t = np.linspace(0, 3, 100)

#Z0 = [1, 1, 0, 0]

#reaction = Reaction.Reaction(Z0, t)
#reaction.graph('concentrations', 'Time (s)', 'Concentration (M)')

# Motion under a gravitational field
#t = np.linspace(0, 50)

#r0 = 1
#v0 = 10

#motion = Gravity.Gravity(r0, v0, t)
#motion.graph('gravity', 'Time (s)', 'Position (m)')

# (Simple) virus spread model
#t = np.linspace(0, 50)

#I0 = 0.01

#P = 1
#ki = 2
#kc = 0.2

#virus = Virus.Virus(I0, P, ki, kc, t)
#virus.graph('virus', 'Time', 'Infected')
