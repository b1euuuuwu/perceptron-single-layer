
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class graph:

	def plotting_decision_regions(selft,X, y, classifier, resolution=0.002):
		
		markers = ('s', 'o', 'x', '^', 'v')
		colors = ('red', 'blue', 'lightred', 'gray', 'cyan')
		cmap = ListedColormap(colors[:len(np.unique(y))])

    	# plot the decision surface
		x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
		x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

		xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
	                           np.arange(x2_min, x2_max, resolution))
		
		
		Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)

		
		Z = Z.reshape(xx1.shape)
		
		plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
		plt.xlim(xx1.min(), xx1.max())
		plt.ylim(xx2.min(), xx2.max())

	    # plot class samples
		for idx, cl in enumerate(np.unique(y)):

			plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), edgecolor='black', marker=markers[idx], label=cl)
		plt.title("Single Layer Perceptron - Decision Regions")
		plt.tight_layout()
		plt.show()
		plt.savefig("result.png")
	def plotting_errors(self,model):

		plt.plot(range(1, len(model.errors_) + 1), model.errors_, marker = 's');
		plt.xlabel("Number of epochs")
		plt.ylabel("Number of actualizations");

		plt.tight_layout()
		plt.show()