from NeuralNetwork import NeuralNetwork

import random
import uuid

class LogicCar :

	speed = 0
	turn = 0
	sensor = [0,0,0,0,0]

	score = 0

	def __init__(self) :
		self.id = uuid.uuid4()
		self.ann = NeuralNetwork()

	def updateSensor(self) :
		#Random update for test

		for i in range(len(self.sensor)) :
			self.sensor[i] = random.uniform(0,1)

	def getSensorValue(self) :
		return self.sensor

	def predictNextConf(self) :
		output = self.ann.getPrediction(self.sensor)
		self.speed = output[0][0]
		self.turn = output[0][1]

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

