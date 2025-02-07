import numpy as np

class perceptron:

    def __init__(self, eta, iterations):

        self.eta = eta;
        self.iterations = iterations;

    def  training(self, data, labels):
    	self.theta = np.zeros(1 + data.shape[1])
    	self.errors_ = []

    	for _ in range(self.iterations):
    		errors = 0;

    		for xi, target in zip(data,labels):

    			update = self.eta * (target - self.predict(xi))
    			self.theta[1:] += update * xi
    			self.theta[0] += update
    			errors += int(update != 0.0)

    		self.errors_.append(errors)

    	return self


    #activation function
    def predict(self, data):
    	phi = np.where(self.calculation_valor_z(data) >= 0.0, 1, -1)
    	return phi

    def calculation_valor_z(self, data):

    	z = np.dot(data, self.theta[1:] + self.theta[0])

    	return z
