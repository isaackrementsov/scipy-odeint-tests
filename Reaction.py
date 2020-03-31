import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Reaction:
	
	def __init__(self, initial_C, t_interval):
		self.t = t_interval
		self.C0 = initial_C
	
	def rxn(self, C, t):
		k1 = 1
		k2 = 1.5

		r1 = k1 * C[0]*C[1]
		r2 = k2 * C[1]*C[2]

		dAdt = -r1
		dBdt = -r1 - r2
		dCdt = r1 - r2
		dDdt = r2

		return [dAdt, dBdt, dCdt, dDdt]
	
	def solve(self):
		Conc = odeint(self.rxn, self.C0, self.t)
		
		return Conc
	
	def graph(self, image_name, x_label, y_label):
		Conc = self.solve()

		cA = Conc[:,0]
		cB = Conc[:,1]
		cC = Conc[:,2]
		cD = Conc[:,2]

		fig = plt.figure(figsize=(10, 8))
		ax = fig.add_subplot(111)
		
		ax.plot(self.t, cA)
		ax.plot(self.t, cB)
		ax.plot(self.t, cC)
		ax.plot(self.t, cD)
		plt.xlabel(x_label)
		plt.ylabel(y_label)

		fig.savefig(image_name + '.png')

