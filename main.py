from files import process_file
from perceptron import perceptron
from ploting import graph


if __name__ == '__main__':

	epochs = 10000;
	eta = 0.01;	#learning factor
	#path dataset
	path = "iris.data"

	obj_plt = graph();
	obj_files = process_file();
	data, labels = obj_files.load_file(path);


	#initialize perceptron
	obj_perceptron = perceptron(eta, epochs)
	#training perceptron
	model = obj_perceptron.training(data,labels);

	#plot errors
	#obj_plt.plotting_errors(model);

	#plot decision regions
	obj_plt.plotting_decision_regions(data, labels, obj_perceptron);

