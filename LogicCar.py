from NeuralNetwork import NeuralNetwork

import random
import uuid

class LogicCar :

	speed = 0
	turn = 0

	score = 0

	def __init__(self) :
		self.id = uuid.uuid4()
		self.ann = NeuralNetwork()

	def getSensorValue(self) :
		return self.sensor

	def predictNextConf(self, sensorValue) :
		output = self.ann.getPrediction(sensorValue)
		self.speed = output[0][0]*50
		self.turn = output[0][1]-0.5

	def getScore(self) :
		return self.score

	def getNetworkLinkWeights(self) :
		allWeights = self.ann.getWeights()
		
		linkWeights = []
		linkWeights.append(allWeights[0])
		linkWeights.append(allWeights[2])
		linkWeights.append(allWeights[4])

		return linkWeights
	
	def setNetworkLinkWeights(self, weights):
		allWeights = self.ann.getWeights()

		allWeights[0] = weights[0].copy()
		allWeights[2] = weights[1].copy()
		allWeights[4] = weights[2].copy()

		self.ann.setWeights(allWeights)

