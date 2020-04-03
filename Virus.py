import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Virus:

	def __init__(self, initial_infected, population_size, infection_k, curing_k, t_interval):
		self.t = t_interval
		self.i0 = initial_infected
		self.imax = population_size
		self.constants = [infection_k, curing_k]
	
	def infections(self, infected, t):
		ki = self.constants[0]
		kc = self.constants[1]

		M = self.imax

		didt = ki*infected*(M - infected) - kc*infected*t
		
		return didt
	
	def solve(self):
		Infected = odeint(self.infections, self.i0, self.t)
		
		return Infected
	
	def graph(self, image_name, x_label, y_label):
		Infected = self.solve()

		fig = plt.figure(figsize=(10, 8))
		ax = fig.add_subplot(111)
		
		ax.plot(self.t, Infected)
		plt.xlabel(x_label)
		plt.ylabel(y_label)

		fig.savefig(image_name + '.png')

