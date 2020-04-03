import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class CircuitLRC:

	def __init__(self, initial_charge, initial_current, resistance, capacitance, inductance, voltage, t_interval):
		self.t = t_interval
		self.initial_values = [initial_charge, initial_current]
		self.C = capacitance
		self.R = resistance
		self.L = inductance 
		self.E = voltage
	
	def circ(self, vars, t):
		Q = vars[0]
		I = vars[1]

		C = self.C
		R = self.R
		L = self.L
		E = self.E

		dQdt = I
		dIdt = (E(t)-I*R-Q/C)/L

		return [dQdt, dIdt]

	def solve(self):
		Circuit = odeint(self.circ, self.initial_values, self.t)
		
		return Circuit
	
	def graph(self, image_name, x_label, y_label):
		Circuit = self.solve()

		I = Circuit[:,1]

		fig = plt.figure(figsize=(10, 8))
		ax = fig.add_subplot(111)
		
		ax.plot(self.t, I)
		plt.xlabel(x_label)
		plt.ylabel(y_label)

		fig.savefig(image_name + '.png')

