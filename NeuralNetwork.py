import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model

class NeuralNetwork :

	def __init__(self) :

		self.model = Sequential()
		self.model.add(Dense(4, input_dim=5, activation='sigmoid'))
		self.model.add(Dense(3, activation='sigmoid'))
		self.model.add(Dense(2, activation='sigmoid'))

		#Output : Speed and Turn

		self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

		plot_model(self.model, show_shapes=True)

	def getPrediction(self, inputValues=[0,0,0,0,0]) :
		inputValues = np.asarray([inputValues], dtype=np.float32)
		return self.model.predict(inputValues)

	def getWeights(self) :
		return self.model.get_weights()

	def setWeights(self, weights) :
		self.model.set_weights(weights)

	def mutation(self,offset) :
		# Change a bit the current weights
		print("Mutation")

if __name__ == "__main__":
	ann = NeuralNetwork()
	print(ann.getPrediction([1,2,3,4,5]))

	weights = ann.getWeights()

	print(weights)

	ann.setWeights(weights)
