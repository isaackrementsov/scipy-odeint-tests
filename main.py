import Reaction
import Gravity
import numpy as np

t = np.linspace(0, 3, 100)
Z0 = [1, 1, 0, 0]
reaction = Reaction.Reaction(Z0, t)
reaction.graph('concentrations', 'Time (s)', 'Concentration (M)')

t = np.linspace(0, 50)
initial_r_v = [1, 10]
reaction = Gravity.Gravity(initial_r_v, t)
reaction.graph('gravity', 'Time (s)', 'Position (m)')