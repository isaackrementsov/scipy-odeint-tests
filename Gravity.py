import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Gravity:

	def __init__(self, initial_radius, initial_velocity, t_interval):
		self.t = t_interval
		self.initial_values = [initial_radius, initial_velocity]

	def force(self, vars, t):
		r = vars[0]
		v = vars[1]

		D = 0.5

		drdt = v
		dvdt = -1/r**2 - D * v**2

		return [drdt, dvdt]

	def solve(self):
		Position = odeint(self.force, self.initial_values, self.t)

		return Position

	def graph(self, image_name, x_label, y_label):
		Position = self.solve()

		r = Position[:,0]

		fig = plt.figure(figsize=(10, 8))
		ax = fig.add_subplot(111)

		ax.plot(self.t, r)
		plt.xlabel(x_label)
		plt.ylabel(y_label)

		fig.savefig(image_name + '.png')
